from pathlib import Path
import hashlib
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

selectedFolder =filedialog.askdirectory(title="Select a Folder")
Folder = Path(selectedFolder)
list_of_Files = []
temp = 0
choice = ''
Hash = ''
fullPath = ''

for item in Folder.iterdir():
    if item.is_dir():
       # print(f"[DIR]  {item.name}")
        list_of_Files.append(item.name)
    elif item.is_file():
        #print(f"[FILE] {item.name}")
        list_of_Files.append(item.name)

print(list_of_Files)

if len(list_of_Files) == 0:
    print("No files or folders found in the selected directory.")
    
    exit()
else:
    for item in list_of_Files:
        print(f"{temp} {item}")
        temp += 1

choice = int(input("Enter the number of the file you want to check the hash of: "))


fullPath = Folder / list_of_Files[choice]
#print(f"{fullPath}")

with open(fullPath, 'rb') as f:
    hash = hashlib.sha256(f.read()).hexdigest()


print(f"{hash}")
