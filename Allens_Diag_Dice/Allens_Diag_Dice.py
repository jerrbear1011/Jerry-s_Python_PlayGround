import tkinter as tk
from pathlib import Path

DTC_Dice_list = []

Diag_Dice_List = []

Recommendation_Work_Dice_List = []


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
        DTC_Dice_list.extend([line.strip() for line in file])
    with open(Diag_Dice_List_path, 'r') as file:
        Diag_Dice_List.extend([line.strip() for line in file])
    with open(Recommendation_Work_Dice_List_path, 'r') as file:
        Recommendation_Work_Dice_List.extend([line.strip() for line in file])
    
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


LoadDefaultItems() ## testing remove later 
Add_Custom_Items() 
ResetToFactory() ## testing remove later

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
window.mainloop()