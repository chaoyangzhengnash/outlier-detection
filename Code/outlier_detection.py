import pandas as pd
import numpy as np 
from tkinter.filedialog import askdirectory

def readCODRs(lst):    
    """Read list of CODR.csv as df."""
    CODR_list = []
    for path in lst:
        CODR_list.append(pd.read_csv(path)[:-2])# remove last 2 rows as they are text
    return CODR_list

def percentile(n):
    """Customized percentile function for agg"""
    def percentile_(x):
        return x.quantile(n)
    percentile_.__name__ = 'percentile_{:2.0f}'.format(n*100)
    return percentile_

def toleranceRate(list_tup,number_tol,percernt_tol,dollar_tol):
    """Load a list of tolerance rate for different UOM"""
    alist = []
    temp = 0
    for tple in list_tup:
        if tple[1] == "Number":
            temp = number_tol
        if tple[1] == "Percent":
            temp = percernt_tol
        if tple[1] == "Dollar":
            temp = dollar_tol
        alist.append(temp)
    return alist

def getLimits(df, new_year, low, high, number_tol, percernt_tol, dollar_tol):     
    """Get limits based on clean and historical data"""   
    limits = pd.DataFrame()    
    # Get limits based on historical and clean data    
    df = df[ (df["REF_DATE"] != new_year) & df["STATUS"].isnull() & df["SYMBOL"].isnull()]    
    # Group by "coordinate" and calculate q_low, q_high, iqr and toleranceRate
    q_low    = df.groupby(["COORDINATE","UOM"])["VALUE"].agg(percentile(low))
    q_high   = df.groupby(["COORDINATE","UOM"])["VALUE"].agg(percentile(high)) 
    q_middle = df.groupby(["COORDINATE","UOM"])["VALUE"].agg(percentile(0.5)) 
    iqr = q_high - q_low
    tolerance = toleranceRate(iqr.index,number_tol, percernt_tol, dollar_tol)    
    # Introduce tolerance parameter
    limits["COORDINATE"] = [tple[0] for tple in q_low.index]
    limits["UOM"]    = [tple[1] for tple in q_low.index]
    limits["median"] = np.array(q_middle)  
    limits["q_low"]  = np.array(q_low)
    limits["q_high"] = np.array(q_high)
    limits["iqr"]    = np.array(iqr)
    limits["lower_bound"]  = np.array(q_low  - (iqr * tolerance))
    limits["higher_bound"] = np.array(q_high + (iqr * tolerance))
    return limits

def getNew(df,new_year,df_limits):
    # Conditioning on latest year
    df = df[df["REF_DATE"] == new_year]
   # t_limits = getLimits(df)
    # Merge new data with limits
    return pd.merge(df, df_limits, how = "left", on = ("COORDINATE","UOM"))
    
def detectOutliers(df):
    # Calculate outlier magnitude
    df['outlier_magnitude'] =  np.where(df['VALUE'] < df['lower_bound'], df['lower_bound'] - df['VALUE'],np.nan)    
    df['outlier_magnitude'] =  np.where(df['VALUE'] > df['higher_bound'], df['VALUE'] - df['higher_bound'],np.nan)    
    # Set outlier flags AND output raws with flag raised
    df['outlier_flag'] = np.where(df['outlier_magnitude'].isnull(), 0,1)
    df = df[df['outlier_flag'] == 1]
    return df

def forward(lst_path, lst_name, new_year, low, high, number_tol, percernt_tol, dollar_tol):
    """Go through the whole process""" 
    # Get output directory
    file_root = askdirectory()   
    CODRS_list = readCODRs(lst_path)
    # iterate to all loaded CODRS
    for i, df in enumerate(CODRS_list):
        df_limits = getLimits(df, new_year, low, high, number_tol, percernt_tol, dollar_tol)
        df_new = getNew(df, new_year, df_limits)
        df_processed = detectOutliers(df_new)
        # save processed files
        output_path = file_root + '\processed_'+ lst_name[i] 
        df_processed.to_csv(output_path)
        




