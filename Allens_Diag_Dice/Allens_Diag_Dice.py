import tkinter as tk

DTC_Dice_list = ['P9999 - Engine on fire','P0FUK - Technician Required','P0420 - Catalytic Converter Efficiency Below Threshold',
              'U2DUM - CAN Bus is being stupid','C1374 - Wheel doing wheel things','U0420 - Received invalid data from some dude named Jimmy',
              'P1602 - Vehicle has become sentient','Try again', "P0300: Random/Multiple Cylinder Misfire Detected",'P0171 - System Too Lean (Bank 1)','P0301 - Cylinder 1 Misfire Detected','P0302 - Cylinder 2 Misfire Detected',]

Diag_Dice_List = ['Car is haunted','Probably the alternator','Needs Premium Air','Has Temu Parts','Bad Ground','Electrical, good luck Allen',
                  'Engine Appers to be made of Engine','Loose connector','Turn Signal is on','Tech is hungover','Vacuum Leak',
                  'Vehicle is shy','Probably the Alternator','Probably NOT the Alternator','Previous Technician','Service writer just wants a commission',
                  'Service writer needs to pay off cruise','Customer wants a loaner','Smells Like Money']

Recommendation_Work_Dice_List = ['Replace entire engine','Consult Mechanic','Perform ECU relearn',
                                 'Do not investigate further','Sacrifice a chicken','Disconnect battery for 10 minutes',
                                 'Replace the ECM module, errr I mean the PCM, Maybe the BCM? honestly, who knows.','Contact priest',
                                 'put in 2 week notice', 'Clear code']


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