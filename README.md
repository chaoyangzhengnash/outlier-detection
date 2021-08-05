# Outlier detection for StatCan CODR tables

## Methodology
The logic is quite straightforward: 
1.	The program reads CODR tables (downloaded via “full cube download”) as a list of data frames.
2.	For each data frame within this list, outlier thresholds (higher and lower bounds) for each series are calculated, using “percentile value + (or -) IQR * tolerance rate”, based on clean (I.e., status and symbol = null) and historical data (ref_date ! = new Year).  
Please noted that users have flexibility to customize the quantile and tolerance rate (by UOM) in the phase of determining the threshold.
3.	After that, outlier thresholds are merged with the new data (simply filtered on ref_date = new year, to be discussed) by UOM, and comparison are implemented to determine if new data (new years’ data) are considered as outlier. 
4.	Finally, csv files are exported on these rows where outlier flag are raised.  


To run this program:
1.	Make sure you have pandas and numpy installed on your python.
2.	Unzip the attachment to any folder, then run the “Main_od.py” in any IDE, it shall pop up an interface. 
3.	In the interface, click “open file” to select a csv file (downloaded via “full cube download” in the prod-environment), or click “open folder” to select a list of csv files (the program will read all csv files within this folder).
4.	Then you shall see the title of selected csv file(s) displacing on the right panel(“tables to be processed”)
5.	Manually entering values of hyper parameters:
a.	New Year: the new reference period available (e.g.2018).
b.	IQR_Low: the quantile set to calculate the IQR (e.g.0.25, which is equivalent to Q1).
c.	IQR_High: the quantile set to calculate the IQR (e.g.0.75, which is equivalent to Q3).
d.	Tolerance_Number: tolerance rate for indicators whose UOM are number (e.g. 1.5).
e.	Tolerance_Percent: tolerance rate for indicators whose UOM are percentage (e.g. 1.3).
f.	Tolerance_Number: tolerance rate for indicators whose UOM are number (e.g. 2).
6.	Click “process and save”, and it will ask you the folder to save the output, after that you shall see the “status” change from “not started” to “start processing!”
7.	Once the “status” changed from “start processing!” to “task done!” (It may take a few minutes), you can found processed file in the defined path.
