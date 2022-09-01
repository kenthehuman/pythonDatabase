import sqlite3
from tkinter import *
from tkinter import ttk


def searchPart():
    pass

def addPart():

    pass

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

# Label
ttk.Label(mainframe, text='Part Number ', width=20).grid(column=1, row=1)

# Entry Fields
# Part number Entry Box
partNumber = StringVar()
partNumber_entry = ttk.Entry(mainframe, width=15,textvariable=partNumber)
partNumber_entry.grid(column=2, row=1)

# Label
ttk.Label(mainframe, text='Part Description ', width=20).grid(column=1, row=2)

# Part description Entry Box
partDescription = StringVar()
partDescription_entry = ttk.Entry(mainframe, width=15,textvariable=partDescription)
partDescription_entry.grid(column=2, row=2, )

# Dwg/Part Number button
# Label
ttk.Label(mainframe, text='Dwg/Part Number ', width=20).grid(column=1, row=3)

# Dwg/Part Numbner Entry Box
partdwg_partNumber = StringVar()
partdwg_partNumber_entry = ttk.Entry(mainframe, width=15, textvariable=partdwg_partNumber)
partdwg_partNumber_entry.grid(column=2, row=3)

# Search Button

# ttk.Button(mainframe, text='Search', command=searchPart).grid(column=2, row=3, sticky=E)
ttk.Button(mainframe, text='Add', command=addPart).grid(column=2)





root.mainloop()
