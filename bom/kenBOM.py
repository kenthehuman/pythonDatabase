# 
from tkinter import *
from tkinter import ttk
import sqlite3

def search_part(*args):
        
    try:
        conn = sqlite3.connect("bom.db")    
        c = conn.cursor()
        value='%'+str(search_entry.get())+'%'
        query = """SELECT * FROM part WHERE part LIKE ?"""
        c.execute(query, (value,))
        rows = c.fetchall()
        i=3
        search_part = ttk.Frame(root, padding="5 5 5 5", relief='sunken')
        search_part.grid()
        for record in rows:
            j=1
            for cell in (range(len(record))):
                ttk.Label(search_part, text=str(record[cell])).grid(row=i+1, column=j+1, padx=4, sticky=W)
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
        c.execute("""SELECT * from parts""")
        rows = c.fetchall()
        i=3
        show = ttk.Frame(root, padding="5 5 5 5")
        show.grid(column=6, row=5)
        for record in rows:
            j=1
            for cell in (range(len(record)-2)):
                ttk.Label(show, text=str(record[cell])).grid(row=i+1, column=j+1, padx=4, sticky=W)
                j+=1
            i += 1
        conn.close()
    except ValueError:
        print("error")
        conn.close()


def bill(*args):
    try:
        conn=sqlite3.connect("bom.db")
        c = conn.cursor()

        # Get part ID of input text
        getPartIDFromIDQuery = "select partID from parts where partNumber=?"
        getPartIDFromIDVar = str(search_entry.get())
        c.execute(getPartIDFromIDQuery, (getPartIDFromIDVar,))
        query_result = c.fetchall()
        
        
        # use bill_partID to get BOM part list
        getPartListFromPartID = "SELECT childID from bomList where parentID = ?"
        c.execute(getPartListFromPartID, query_result[0])
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
ttk.Button(mainframe, text="Show bill", command=bill).grid(column=4, row=1, sticky=E)

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

search_entry.focus()
root.bind("<Return>", search_part)

root.mainloop()



# Get part ID of input text
getPartIDFromIDQuery = "select partID from parts where partNumber=?"
getPartIDFromIDVar = "DC202-a"
c.execute(getPartIDFromIDQuery, (getPartIDFromIDVar,))
query_result = c.fetchall()
bill_partID = query_result[0][0] # strips from list, set thing

# use bill_partID to get BOM part list
getPartListFromPartID = "SELECT childID from bomList where parentID = ?"
c.execute(getPartListFromPartID, query_result[0])
partID_list = c.fetchall()

# return rows with previous results
c.execute("SELECT partID, partName, partDescription, partNumber from parts where partID = ? or partID = ? or partID = ?;", partID_list)