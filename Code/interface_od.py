
import tkinter as tk
import button_method as bm

# Design the interface
def go():
    window = tk.Tk()
    window.title("CODR tables- Outlier detection")
    window.rowconfigure(0, weight=1)
    window.columnconfigure(0,  weight=1)

    """ Set frames """
    fr_labels_1  = tk.Frame(window, relief=tk.RIDGE, bd=2)
    fr_labels_2  = tk.Frame(window, relief=tk.RIDGE, bd=2)
    fr_buttons_1 = tk.Frame(window, relief=tk.RAISED, bd=2)
    
    """ Set labels """
    #Set labels for general information
    lbl_title_info = tk.Label(master = fr_labels_1, text = "General information", 
                              fg = "white", bg = "black")
    lbl_Guid_1     = tk.Label(master = fr_labels_1, text = "CODR tables:")
    lbl_Result_1   = tk.Label(master = fr_labels_1, text = "Null")
    lbl_Status_info = tk.Label(master = fr_labels_1, text = "Status:")
    lbl_Status_curr = tk.Label(master = fr_labels_1, text = "Not start")
    #Set for labels for hyper parameter
    lbl_title_para = tk.Label(master = fr_labels_2, text = "Hyper parameter", 
                              fg = "white", bg = "black")
    lbl_new_year  = tk.Label(master = fr_labels_2, text = "New year(eg:2018)")
    lbl_iqr_low  = tk.Label(master = fr_labels_2, text = "IQR_Low(0~1)")
    lbl_iqr_high = tk.Label(master = fr_labels_2, text = "IQR_High(0~1)")
    lbl_tol_num = tk.Label(master = fr_labels_2, text = "Tolerance_Number")
    lbl_tol_per = tk.Label(master = fr_labels_2, text = "Tolerance_Percent")
    lbl_tol_dol = tk.Label(master = fr_labels_2, text = "Tolerance_Dollar")
    
    """ Set entries """
    ent_new_year  = tk.Entry(master=fr_labels_2, width=5)
    #IQR thresold
    ent_iqr_low  = tk.Entry(master=fr_labels_2, width=5)
    ent_iqr_high = tk.Entry(master=fr_labels_2, width=5)
    #Tolerance rate
    ent_tol_num = tk.Entry(master=fr_labels_2, width=5)
    ent_tol_per = tk.Entry(master=fr_labels_2, width=5)
    ent_tol_dol = tk.Entry(master=fr_labels_2, width=5)
    
    """ Set buttons """ 
    btn_open_csv = tk.Button(fr_buttons_1, text="Open file",
                             command = lambda:bm.openSingleCsv(lbl_Result_1))
    btn_open_fol = tk.Button(fr_buttons_1, text="Open folder",
                             command = lambda:bm.openFolder(lbl_Result_1))
    btn_proc_sav = tk.Button(fr_buttons_1, text="Process and save",
                             command = lambda:bm.processSave(lbl_Status_curr,
                                                             float(ent_new_year.get()),
                                                             float(ent_iqr_low.get()),float(ent_iqr_high.get()),
                                                             float(ent_tol_num.get()),float(ent_tol_per.get()),float(ent_tol_dol.get())))
    
    """ Attach widgets to frames through grid""" 
    #  Attach widgets for general information
    lbl_title_info.grid(row=0, column=0, sticky="w")
    lbl_Guid_1.grid(row=1, column=0, sticky="ns")
    lbl_Result_1.grid(row=1, column=1, sticky="ns")
    lbl_Status_info.grid(row=2, column=0, sticky="ew")
    lbl_Status_curr.grid(row=2, column=1, sticky="ew")
    
    #  Attach widgets for hyper parameters labels and entries
    #   -Lables
    lbl_title_para.grid(row=3, column=0, sticky="w") 
    lbl_new_year.grid(row=4, column=0, sticky="ew") 
    lbl_iqr_low.grid(row=5, column=0, sticky="ew")  
    lbl_iqr_high.grid(row=6, column=0, sticky="ew")
    
    lbl_tol_num.grid(row=4, column=2, sticky="ew")
    lbl_tol_per.grid(row=5, column=2, sticky="ew")
    lbl_tol_dol.grid(row=6, column=2, sticky="ew")
    #   -Entries
    ent_new_year.grid(row=4, column=1, sticky="ew")
    ent_iqr_low.grid(row=5, column=1, sticky="ew")
    ent_iqr_high.grid(row=6, column=1, sticky="ew")
    
    ent_tol_num.grid(row=4, column=3, sticky="ew")
    ent_tol_per.grid(row=5, column=3, sticky="ew")
    ent_tol_dol.grid(row=6, column=3, sticky="ew")
    
    #  Attach buttons
    btn_open_csv.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
    btn_open_fol.grid(row=0, column=1, sticky="ew", padx=5, pady=5)
    btn_proc_sav.grid(row=0, column=2, sticky="ew", padx=5, pady=5)
    """ Attach frams to windows """ 
    fr_labels_1.grid(row=0, column=0, sticky="nsew")
    fr_labels_2.grid(row=1, column=0, sticky="nsew")
    fr_buttons_1.grid(row=2, column=0, sticky="nsew")
    window.mainloop()
    
