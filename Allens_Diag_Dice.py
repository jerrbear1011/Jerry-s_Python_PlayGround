import tkinter as tk

DTC_Dice_list = ['P9999 - Engine on fire','P0FUK - Technician Required','P0420 - Catalytic Converter Efficiency Below Threshold',
              'U2DUM - CAN Bus is being stupid','C1374 - Wheel doing wheel things','U0420 - Received invalid data from some dude named Jimmy',
              'P1602 - Vehicle has become sentient','Try again']

Diag_Dice_List = ['Car is haunted','Probably the alternator','Needs Premium Air','Has Temu Parts','Bad Ground','Electrical, good luck Allen',
                  'Engine Appers to be made of Engine','Loose connector','Turn Signal is on','Tech is hungover','Vacuum Leak',
                  'Vehicle is shy','Probably the Alternator','Probably NOT the Alternator','Previous Technician','Service writer just wants a commission',
                  'Service writer needs to pay off cruise','Customer wants a loaner']

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
    DTC_label.config(text="Diagnostic Trouble Code: " + DTCRoll)
    Diagroll_label.config(text="Diagnosis: " + Diagroll)
    RecRoll_label.config(text="Recommendation: " + RecRoll)

## start Gui 
window = tk.Tk()
window.title("Vehicle Diagnostic Analyzer")
window.geometry("800x700")

## title
title = tk.Label(window, text="Vehicle Diagnostic Analyzer", font=("Arial", 24, "bold"))
title.pack(pady=20)
button = tk.Button(window, text="Roll for Diagnostic", font=("Arial", 16), command=Run_Diags)
button.pack(pady=20)

#results 
results_frame = tk.Frame(window)
results_frame.pack(pady=20)

DTC_label = tk.Label(results_frame, text="Diagnostic Trouble Code: ---", font=("Arial", 16), wraplength = 700)
DTC_label.pack(pady=10)

Diagroll_label = tk.Label(results_frame, text="Diagnosis: ---" , font=("Arial", 16), wraplength = 700)
Diagroll_label.pack(pady=10)

RecRoll_label = tk.Label(results_frame, text="Recommendation: ---" , font=("Arial", 16), wraplength = 700)
RecRoll_label.pack(pady=10)

window.mainloop()







