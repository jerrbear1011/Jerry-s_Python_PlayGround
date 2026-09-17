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


def save_dtc(new_dtc, dtc_listbox, add_window):
    Directory = Path(__file__).resolve().parent
    DTC_Dice_list_path = Directory / 'CustomItems' / 'DTC_Dice_list_Custom.txt'
    if new_dtc.strip():
        DTC_Dice_list_custom.append(new_dtc.strip())
        dtc_listbox.insert(tk.END, new_dtc.strip())
        add_window.destroy()
        with open(DTC_Dice_list_path, 'a') as file:
            file.write(new_dtc.strip()+ "\n")
    DTC_Dice_list.clear()
    Add_Custom_Items()

def save_diag(new_diag, diag_listbox, add_window):
    Directory = Path(__file__).resolve().parent
    Diag_Dice_List_path = Directory / 'CustomItems' / 'Diag_Dice_List_Custom.txt'
    if new_diag.strip():
        Diag_Dice_List_Custom.append(new_diag.strip())
        diag_listbox.insert(tk.END, new_diag.strip())
        add_window.destroy()
        with open(Diag_Dice_List_path, 'a') as file:
            file.write(new_diag.strip() + "\n")
    Diag_Dice_List_Custom.clear()
    Add_Custom_Items()

def save_Rec(new_rec, diag_listbox, add_window):
    Directory = Path(__file__).resolve().parent
    Recommendation_Work_Dice_List_path = Directory / 'CustomItems' / 'Recom_Work_Dice_List_Custom.txt'
    if new_rec.strip():
        Recommendation_Work_Dice_List_Custom.append(new_rec.strip())
        diag_listbox.insert(tk.END, new_rec.strip())
        add_window.destroy()
        with open(Recommendation_Work_Dice_List_path, 'a') as file:
            file.write(new_rec.strip() + "\n")
    Recommendation_Work_Dice_List_Custom .clear()
    Add_Custom_Items()

def ButtonTest():
    print("click")

def deleteItem(ListSelect, IdexSelect):
    Directory = Path(__file__).resolve().parent

def deleteItem(ListSelect, IdexSelect):
    ListsOfLists = [DTC_Dice_list_custom, Diag_Dice_List_Custom, Recommendation_Work_Dice_List_Custom]
    Directory = Path(__file__).resolve().parent
    FilePaths = [
        Directory / 'CustomItems' / 'DTC_Dice_list_custom.txt',
        Directory / 'CustomItems' / 'Diag_Dice_List_Custom.txt',
        Directory / 'CustomItems' / 'Recom_Work_Dice_List_Custom.txt'
    ]

    targetList = ListsOfLists[ListSelect]
    targetPath = FilePaths[ListSelect] 
    if not targetList:
        return 
        
    del targetList[IdexSelect]

    with open(targetPath, "w") as file:
        for item in targetList:
            file.write(f"{item}\n")
            


LoadDefaultItems()  
Add_Custom_Items() 
#deleteItem(1,0) ## testing remove later
#ResetToFactory() ## testing remove later


def add_dtc(config_window, dtc_listbox):
    add_window = tk.Toplevel(config_window)
    add_window.title("Add DTC")
    add_window.geometry("400x150")
    tk.Label(add_window, text="Enter new DTC:").pack(pady =10)

    dtc_entry = tk.Entry(add_window, width=45)
    dtc_entry.pack()

    tk.Button(
        add_window,
        text='save',
        command=lambda: save_dtc(dtc_entry.get(), dtc_listbox, add_window)
    ).pack(pady=10)

def add_diag(config_window, diag_listbox):
    add_window = tk.Toplevel(config_window)
    add_window.title("Add Diag")
    add_window.geometry("400x150")
    tk.Label(add_window, text="Enter new Diag:").pack(pady =10)

    diag_entry = tk.Entry(add_window, width=45)
    diag_entry.pack()

    tk.Button(
        add_window,
        text='save',
        command=lambda: save_diag(diag_entry.get(), diag_listbox, add_window)
    ).pack(pady=10)

def add_rec(config_window, Rec_listbox):
    add_window = tk.Toplevel(config_window)
    add_window.title("Add Recommendation")
    add_window.geometry("400x150")
    tk.Label(add_window, text="Enter new recommendation:").pack(pady =10)

    diag_entry = tk.Entry(add_window, width=45)
    diag_entry.pack()

    tk.Button(
        add_window,
        text='save',
        command=lambda: save_Rec(diag_entry.get(), Rec_listbox, add_window)
    ).pack(pady=10)

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
    dtc_listbox.pack(fill="both", expand=True)
    dtc_frame.pack(fill="both", expand=True, padx=10, pady=10)
    for item in DTC_Dice_list_custom:
        dtc_listbox.insert(tk.END, item)


    DTC_button_frame = tk.Frame(dtc_frame)
    DTC_button_frame.pack()

    DTC_add_button = tk.Button(DTC_button_frame,
                                text="Add",
                                command=lambda: add_dtc(config_window, dtc_listbox))
    DTC_add_button.pack(side="left")

    #DTC_edit_button = tk.Button(DTC_button_frame, text="Edit", command=ButtonTest)
    #DTC_edit_button.pack(side="left")

    DTC_delete_button = tk.Button(DTC_button_frame, text="Delete", command=ButtonTest)
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
    Diag_listbox.pack(fill="both", expand=True)
    Diag_frame.pack(fill="both", expand=True, padx=10, pady=10)
    for item in Diag_Dice_List_Custom:
            Diag_listbox.insert(tk.END, item)

    Diag_button_frame = tk.Frame(Diag_frame)
    Diag_button_frame.pack()

    Diag_add_button = tk.Button(Diag_button_frame, text="Add", command=lambda: add_diag(config_window, Diag_listbox))
    Diag_add_button.pack(side="left")

    #Diag_edit_button = tk.Button(Diag_button_frame, text="Edit", command=ButtonTest)
    #Diag_edit_button.pack(side="left")

    Diag_delete_button = tk.Button(Diag_button_frame, text="Delete", command=ButtonTest)
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

    Rec_listbox.pack(fill="both", expand=True)
    Rec_frame.pack(fill="both", expand=True, padx=10, pady=10)
    for item in Recommendation_Work_Dice_List_Custom:
            Rec_listbox.insert(tk.END, item)



    rec_button_frame = tk.Frame(Rec_frame)
    rec_button_frame.pack()

    rec_add_button = tk.Button(rec_button_frame, text="Add", command=lambda: add_rec(config_window, Rec_listbox))
    rec_add_button.pack(side="left")

    #rec_edit_button = tk.Button(rec_button_frame, text="Edit", command=ButtonTest)
    #rec_edit_button.pack(side="left")

    rec_delete_button = tk.Button(rec_button_frame, text="Delete", command=ButtonTest)
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