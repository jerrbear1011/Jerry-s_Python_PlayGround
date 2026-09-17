import tkinter as tk
from pathlib import Path

DTC_Dice_list = []

DTC_Dice_list_custom = []

Diag_Dice_List = []

Diag_Dice_List_Custom = []

Recommendation_Work_Dice_List = []

Recommendation_Work_Dice_List_Custom = []


def Diagnostic_Dice():
    import random
    Diagroll = random.choice(Diag_Dice_List)
    RecRoll = random.choice(Recommendation_Work_Dice_List)
    DTCRoll = random.choice(DTC_Dice_list)
    ##print(f"Test Click")
    return DTCRoll, Diagroll, RecRoll 

def Run_Diags():
    DTCRoll, Diagroll, RecRoll = Diagnostic_Dice()
    DTC_label.config(text= DTCRoll)
    Diagroll_label.config(text= Diagroll)
    RecRoll_label.config(text=RecRoll)

def LoadDefaultItems():
    global DTC_Dice_list, Diag_Dice_List, Recommendation_Work_Dice_List
    Directory = Path(__file__).resolve().parent
    DTC_Dice_list_path = Directory / 'ReadOnly' / 'DTC_Dice_list_RO.txt'
    Diag_Dice_List_path = Directory / 'ReadOnly' / 'Diag_Dice_List_RO.txt'
    Recommendation_Work_Dice_List_path = Directory / 'ReadOnly' / 'Recom_Work_Dice_List_RO.txt'

    with open(DTC_Dice_list_path, 'r') as file:
        DTC_Dice_list = [line.strip() for line in file]
    with open(Diag_Dice_List_path, 'r') as file:
        Diag_Dice_List = [line.strip() for line in file]
    with open(Recommendation_Work_Dice_List_path, 'r') as file:
        Recommendation_Work_Dice_List = [line.strip() for line in file]

    #print (DTC_Dice_list, Diag_Dice_List, Recommendation_Work_Dice_List)

def Add_Custom_Items():
    global DTC_Dice_list, Diag_Dice_List, Recommendation_Work_Dice_List
    Directory = Path(__file__).resolve().parent
    DTC_Dice_list_path = Directory / 'CustomItems' / 'DTC_Dice_list_Custom.txt'
    Diag_Dice_List_path = Directory / 'CustomItems' / 'Diag_Dice_List_Custom.txt'
    Recommendation_Work_Dice_List_path = Directory / 'CustomItems' / 'Recom_Work_Dice_List_Custom.txt'
    
    with open(DTC_Dice_list_path, 'r') as file:
        item = [line.strip() for line in file]
        DTC_Dice_list.extend(item)
        DTC_Dice_list_custom.extend(item)
      #  print(f"Custom DTC List: {DTC_Dice_list_custom}")
    with open(Diag_Dice_List_path, 'r') as file:
        item = [line.strip() for line in file]
        Diag_Dice_List.extend(item)
        Diag_Dice_List_Custom.extend(item)
    with open(Recommendation_Work_Dice_List_path, 'r') as file:
        item = [line.strip() for line in file]
        Recommendation_Work_Dice_List.extend(item)
        Recommendation_Work_Dice_List_Custom.extend(item)

def ResetToFactory():
    global DTC_Dice_list, Diag_Dice_List, Recommendation_Work_Dice_List
    DTC_Dice_list.clear()
    Diag_Dice_List.clear()
    Recommendation_Work_Dice_List.clear()
    Directory = Path(__file__).resolve().parent
    DTC_Dice_list_path = Directory / 'CustomItems' / 'DTC_Dice_list_Custom.txt'
    Diag_Dice_List_path = Directory / 'CustomItems' / 'Diag_Dice_List_Custom.txt'
    Recommendation_Work_Dice_List_path = Directory / 'CustomItems' / 'Recom_Work_Dice_List_Custom.txt'

    with open(DTC_Dice_list_path, 'w') as file:
        pass
    with open(Diag_Dice_List_path, 'w') as file:
        pass    
    with open(Recommendation_Work_Dice_List_path, 'w') as file:
        pass
    LoadDefaultItems()


LoadDefaultItems()  
Add_Custom_Items() 
#ResetToFactory() ## testing remove later

def openConfig():
    config_window = tk.Toplevel(window)
    config_window.title("Configuration")   
    config_window.geometry("600x850")
    dtc_frame = tk.LabelFrame(
        config_window,
        text=" Diagnostic Trouble Codes (DTC) ",
        font=("Arial", 12, "bold"),
        padx=10,
        pady=10
    )
    dtc_listbox = tk.Listbox(
        dtc_frame
    )
    dct_listbox = tk.Listbox(
        dtc_frame
    )
    dct_listbox.pack(fill="both", expand=True)
    dtc_frame.pack(fill="both", expand=True, padx=10, pady=10)
    for item in DTC_Dice_list_custom:
        dct_listbox.insert(tk.END, item)


    DTC_button_frame = tk.Frame(dtc_frame)
    DTC_button_frame.pack()

    DTC_add_button = tk.Button(DTC_button_frame, text="Add",command=ResetToFactory)
    DTC_add_button.pack(side="left")

    DTC_edit_button = tk.Button(DTC_button_frame, text="Edit")
    DTC_edit_button.pack(side="left")

    DTC_delete_button = tk.Button(DTC_button_frame, text="Delete")
    DTC_delete_button.pack(side="left")


    
    #add_DCT_button = tk.Button(
     #   config_window,
      #  text="Add DCT Item",
       # command=Add_DTC
    #)
    #add_DCT_button.pack(pady=10)

    #del_DCT_button = tk.Button(
      #      config_window,
    #        text="Delete DCT Item",
     #      # command=Add_DTC
    #    )
    #del_DCT_button.pack(pady=10)

    Diag_frame = tk.LabelFrame(
        config_window,
        text=" Diagnostic Items ",
        font=("Arial", 12, "bold"),
        padx=10,
        pady=10
    )
    Diag_listbox = tk.Listbox(
        Diag_frame
    )
    Diag_listbox = tk.Listbox(
        Diag_frame
    )
    Diag_listbox.pack(fill="both", expand=True)
    Diag_frame.pack(fill="both", expand=True, padx=10, pady=10)
    for item in Diag_Dice_List_Custom:
            Diag_listbox.insert(tk.END, item)

    Diag_button_frame = tk.Frame(Diag_frame)
    Diag_button_frame.pack()

    Diag_add_button = tk.Button(Diag_button_frame, text="Add")
    Diag_add_button.pack(side="left")

    Diag_edit_button = tk.Button(Diag_button_frame, text="Edit")
    Diag_edit_button.pack(side="left")

    Diag_delete_button = tk.Button(Diag_button_frame, text="Delete")
    Diag_delete_button.pack(side="left")



    #add_Diag_button = tk.Button(
    #    config_window,
    #    text="Add Diagnostic Item",
       # command=Add_DTC
    #)
    #add_Diag_button.pack(pady=10)

    #del_Diag_button = tk.Button(
    #        config_window,
    #        text="Delete Diagnostic Item",
    #       # command=Add_DTC
    #    )
    #del_Diag_button.pack(pady=10)

    Rec_frame = tk.LabelFrame(
            config_window,
            text=" Recommended Repairs ",
            font=("Arial", 12, "bold"),
            padx=10,
            pady=10
        )
    Rec_listbox = tk.Listbox(
        Rec_frame
    )
    Rec_listbox = tk.Listbox(
        Rec_frame
    )
    Rec_listbox.pack(fill="both", expand=True)
    Rec_frame.pack(fill="both", expand=True, padx=10, pady=10)
    for item in Recommendation_Work_Dice_List_Custom:
            Rec_listbox.insert(tk.END, item)



    rec_button_frame = tk.Frame(Rec_frame)
    rec_button_frame.pack()

    rec_add_button = tk.Button(rec_button_frame, text="Add")
    rec_add_button.pack(side="left")

    rec_edit_button = tk.Button(rec_button_frame, text="Edit")
    rec_edit_button.pack(side="left")

    rec_delete_button = tk.Button(rec_button_frame, text="Delete")
    rec_delete_button.pack(side="left")
    

   # add_REC_button = tk.Button(
   #     config_window,
   #     text="Add Recommended Repair",
       # command=Add_DTC
    #)
    #add_REC_button.pack(pady=10)

    #del_REC_button = tk.Button(
    #    config_window,
    #    text="Delete Recommended Repair",
       # command=Add_DTC
    #)
    #del_REC_button.pack(pady=10)

## start Gui 
window = tk.Tk()
window.title("Vehicle Diagnostic Analyzer")
window.geometry("800x500")

## title
#title = tk.Label(window, text="Vehicle Diagnostic Analyzer", font=("Arial", 24, "bold"))
#title.pack(pady=20)
header_frame = tk.Frame(window, relief="raised", borderwidth=2)
header_frame.pack(fill="x", padx=10, pady =10)
title = tk.Label(header_frame, 
                 text="Vehicle Diagnostic Analyzer",
                 font=("Arial", 20, "bold"))
title.pack(pady=10)

button = tk.Button(window, 
                   text="Roll for Diagnostic", 
                   font=("Arial", 16, "bold"),
                   padx=20,
                   pady=10,
                   command=Run_Diags)
button.pack(pady=(20, 0))

#results 
results_frame = tk.LabelFrame(
    window, 
    text=" Diagnostic Results ", 
    font = ("arial", 12, "bold"), 
    padx=15, 
    pady=15)
results_frame.pack(fill= "x", padx=20, pady=(5,20))
#results_frame.pack_propagate(False)

DTC_title = tk.Label(
    results_frame,
    text="Diagnostic Trouble Code",
    font=("Arial", 11, "bold"),
    anchor="w"
)
DTC_title.pack(fill="x")
DTC_label = tk.Label(
    results_frame,
    text="---",
    font=("Arial", 16),
    anchor="w",
    wraplength=700,
    justify="left"
)
DTC_label.pack(fill="x", pady=(0, 15))

Diag_title = tk.Label(
    results_frame,
    text="DIAGNOSIS",
    font=("Arial", 11, "bold"),
    anchor="w"
)
Diag_title.pack(fill="x")
Diagroll_label = tk.Label(
    results_frame,
    text="---",
    font=("Arial", 16),
    anchor="w",
    wraplength=700,
    justify="left"
)
Diagroll_label.pack(fill="x", pady=(0, 15))

Rec_title = tk.Label(
    results_frame,
    text="RECOMMENDED REPAIR",
    font=("Arial", 11, "bold"),
    anchor="w"
)
Rec_title.pack(fill="x")
RecRoll_label = tk.Label(
    results_frame,
    text="---",
    font=("Arial", 16),
    anchor="w",
    wraplength=700,
    justify="left"
)
RecRoll_label.pack(fill="x")

Status_bar = tk.Label(
    window,
    text="Status: Ready",
    relief="sunken",
    anchor="w"
)
Status_bar.pack(side="bottom", fill="x")

config_button = tk.Button(
    window,
    text="Configuration",
    font=("Arial", 12),
    padx=10,
    pady=5,
    command=openConfig
)
config_button.pack()
window.mainloop()