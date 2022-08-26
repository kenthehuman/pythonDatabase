import sqlite3
from tkinter import *
from tkinter import ttk


# connect to database
con = sqlite3.connect('bom.db')
cur = con.cursor()


# main application window
root = Tk()
root.title("BillofMaterials")

# Content Frame
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, S, W, E))
root.columnconfigure(0, weight=0)
root.rowconfigure(0, weight=1)

# Entry Fields
# 

create table 

root.mainloop()
