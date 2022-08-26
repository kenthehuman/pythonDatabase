from tkinter import *
from tkinter import ttk
import sqlite3


# some querys
# con = sqlite3.connect("bom.db")
# c = con.cursor()
# c.execute("select * from parts")
# c.fetchall()

# c.execute("""SELECT p.partID, p.partDescription, bl.qtyUsed
# FROM parts AS p, bomList AS bl
# WHERE p.partID=28;""")