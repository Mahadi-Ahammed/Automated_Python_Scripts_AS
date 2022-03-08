import os
import tkinter as tk
def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)
        

from tkinter import filedialog
root = tk.Tk()
root.withdraw()
file_path = filedialog.askdirectory()

a=int(input("How many folder do you want to create: "))
for i in range(a):
    name=input("folder name:" )
    createFolder(file_path+'/'+name+'/')
