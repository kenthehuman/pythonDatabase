from tkinter import *
from tkinter import ttk
import sqlite3

def search_part(*args):
        
    try:
        conn = sqlite3.connect("bom.db")    
        c = conn.cursor()
        value=str(search_entry.get())
        query = """SELECT * FROM part WHERE part=?"""
        c.execute(query, (value,))
        rows = c.fetchall()
        i=3
        search_part = ttk.Frame(root, padding="5 5 5 5")
        for record in rows:
            j=1
            for cell in (range(len(record))):
                print(i)
                ttk.Label(mainframe, text=str(record[cell])).grid(row=i+1, column=j+1, padx=4, sticky=W)
                j+=1
            i += 1
        conn.close()
    except ValueError:
        print('error')
        conn.close()
        pass


def show_all():
    try:
        conn=sqlite3.connect("bom.db")
        c = conn.cursor()
        c.execute("""SELECT * from part""")
        rows = c.fetchall()
        i=3
        show = ttk.Frame(root, padding="5 5 5 5")
        show.grid(column=6, row=5)
        for record in rows:
            j=1
            for cell in (range(len(record)-2)):
                print(i)
                ttk.Label(show, text=str(record[cell])).grid(row=i+1, column=j+1, padx=4, sticky=W)
                j+=1
            i += 1
        conn.close()
    except ValueError:
        print("error")
        conn.close()


root = Tk()
root.title("Bill of Materials")
# Main frame window
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

search = StringVar()
search_entry = ttk.Entry(mainframe, width = 12, textvariable=search)
search_entry.grid(column=1, row=1, sticky=(W,E))

ttk.Button(mainframe, text="Search", command=search_part).grid(column=2, row=1, sticky=W)
ttk.Button(mainframe, text="Show All", command=show_all).grid(column=3, row=1, sticky=W)

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

search_entry.focus()
root.bind("<Return>", search_part)

root.mainloop()