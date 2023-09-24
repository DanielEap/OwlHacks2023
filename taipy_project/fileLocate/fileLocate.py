import tkinter as tk
from tkinter import filedialog

def fileLocate():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    return file_path

#fileLocate()
print(fileLocate())
