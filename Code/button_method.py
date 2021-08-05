import os
import outlier_detection as od
import timeit
from tkinter.filedialog import askopenfilename, askdirectory

list_CODRs_path = list()
list_CODRs_name = list()

def openSingleCsv(lbl):
    """Open a file for editing."""
    CODR_path = askopenfilename(
        filetypes=[("CSV Files", "*.csv"), ("All Files", "*.*")])
    list_CODRs_name.append(os.path.split(CODR_path)[1])
    list_CODRs_path.append(CODR_path)
    lbl["text"] = f"{str(list_CODRs_name)}"
    
def openFolder(lbl):
    """Open a folder and read all CODR tables for editing."""
    folder_path = askdirectory(title='Select Folder') 
    for root, dirs, filenames in os.walk(folder_path):
        for file in filenames:
            if not file.endswith("_MetaData.csv"):
                list_CODRs_name.append(file)
                list_CODRs_path.append(os.path.join(root, file))
                lbl["text"] = f"{str(list_CODRs_name)}"

def processSave(lbl,new_year, low, high, number_tol, percernt_tol, dollar_tol):
    start = timeit.default_timer()    
    lbl["text"] = "Start processing!"
    lbl.update()    
    od.forward(list_CODRs_path, list_CODRs_name, 
               new_year, low, high, 
               number_tol, percernt_tol, dollar_tol)    
    lbl["text"] = "Task done!"    
    stop = timeit.default_timer()
    print('Time: ', stop - start)      