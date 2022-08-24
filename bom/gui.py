"""from tkinter import *
from tkinter import ttk
import sqlite3
import tkinter
from turtle import st

# Function to add the new index to the database
# Insert from values entered in form (entry fields, labels)
def submit():
    connection = sqlite3.connect("bom.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO part(part,description,part_number) VALUES (?,?,?)",(item_part.get(),item_description.get(),item_number.get()))
    connection.commit()
    connection.close()
    item_part.delete(0, END)
    item_description.delete(0, END)
    item_number.delete(0, END)


# Show indexs, selects all columns
def query():
    global query_window
    query_window = Tk()
    query_window.geometry("1000x900")
    query_window.title("indexs")
    connection = sqlite3.connect("bom.db")
    cursor = connection.cursor()
    cursor.execute("SELECT *, oid FROM part")
    indexs = cursor.fetchall()
    print(indexs)
    print_indexs = []
    i=0
    j=0
    for index in indexs:
        j=0
        for cell in (range(len(index)-2)):
            print(i)
            ttk.Label(query_window, text=str(index[cell])).grid(row=i+1, column=j+1, padx=4, sticky=W)
            j+=1
        i += 1
        # print_indexs += str(index[0]) + ", " + str(index[1]) + " , " + str(index[2]) + ", " + "\t" + str(index[3]) +"\n"
    # query_label = Label(query_window, text=print_indexs)
    # query_label.grid(row=0, column=0)

    connection.commit()
    connection.close()


def update():
    connection = sqlite3.connect("bom.db")
    cursor = connection.cursor()
    index_id = select_box.get()

    cursor.execute(
        'UPDATE part SET part=?, description=?, part_number=? WHERE oid=?',
        (item_part_editor.get(),item_description_editor.get(),item_part_number_editor.get(),index_id)
    )
    connection.commit()
    connection.close()
    editor.destroy()

def edit():
    global editor
    editor = Tk()
    editor.geometry("450x125")
    editor.title("Edit Part")
    connection = sqlite3.connect("bom.db")
    cursor = connection.cursor()
    index_id = select_box.get()

    cursor.execute("SELECT * FROM part WHERE oid=?",(index_id))
    indexs = cursor.fetchall()

    global item_part_editor
    global item_description_editor
    global item_part_number_editor

    item_part_editor = Entry(editor, width=20)
    item_part_editor.grid(row=0, column=1, sticky=W)
    item_description_editor = Entry(editor, width=20)
    item_description_editor.grid(row=1, column=1, sticky=W)
    item_part_number_editor = Entry(editor, width=20)
    item_part_number_editor.grid(row=2, column=1, sticky=W)

    item_part_label_editor = Label(editor, text='part ')
    item_part_label_editor.grid(row=0, column=0, sticky=E)
    item_description_label_editor = Label(editor,  text='Quantity ')
    item_description_label_editor.grid(row=1, column=0, sticky=E)
    item_part_number_label_editor = Label(editor, text ='Price ($) ')
    item_part_number_label_editor.grid(row=2,column=0, sticky=E)

    for index in indexs:
        item_part_editor.insert(0, index[0])
        item_description_editor.insert(0, index[1])
        item_part_number_editor.insert(0, index[2])
    save_btn = Button(editor, text="Save index", command=update)
    save_btn.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=145)
    connection.commit()
    connection.close()

# Delete a index
# This function runs based on the ID specified in the ‘Select ID’ form
def delete():
    connection = sqlite3.connect("bom.db")
    cursor = connection.cursor()
    cursor.execute("DELETE from part WHERE oid=?",(select_box.get()))
    connection.commit()
    connection.close()


# Create main window
window = Tk()
window.geometry("400x450")
window.title("Summary")


# Create the entry fields, labels, functions, and buttons to access the database
# Add a index to the database
item_part = Entry(window, width=20)
item_part.grid(row=0, column=1, pady=2, sticky=W)
item_description = Entry(window, width=20)
item_description.grid(row=1, column=1, pady=2, sticky=W)
item_number = Entry(window, width=20)
item_number.grid(row=2, column=1, pady=2, sticky=W)

item_part_label = Label(window, text='Name ')
item_part_label.grid(row=0, column=0, pady=2, sticky=W)
item_description_label = Label(window, text='Description ')
item_description_label.grid(row=1, column=0, pady=2, sticky=W)
item_number_label = Label(window, text='Part Number ')
item_number_label.grid(row=2, column=0, pady=2, sticky=E)


# Clickable button for submitting adding index
submit_btn = Button(window, text="Add index to Database", command=submit)
submit_btn.grid(row=3, column=0, columnspan=2, pady=2)

# Clickable button for showing indexs
query_btn = Button(window, text="Show indexs", command=query)
query_btn.grid(row=4, column=0, columnspan=2, pady=2)

# Update based on the ID specified in the 'Select ID' field
select_box=Entry(window, width=20)
select_box.grid(row=6, column=1, pady=2, sticky=W)

select_box_label = Label(window, text='Select ID ')
select_box_label.grid(row=6, column=0, pady=2, sticky=E)

# Create the button for updating indexs
edit_btn = Button(window, text="Update index", command=edit)
edit_btn.grid(row=11, column=0, columnspan=2, pady=2)

# Create delete index button
delete_btn = Button(window, text="Delete index", command=delete)
delete_btn.grid(row=12, column=0, columnspan=2, pady=2)

# Close button
# window.destroy closes that application
close_btn=Button(window,text="Close",command=window.destroy)
close_btn.grid(row=13, column =0, columnspan=2, pady=2)

window.mainloop()


# loop to make a bunch of widgets
def open():
    root = Tk()
    for i in range(4):
        ttk.Button(root, text="Hello "+str(i)).grid(row=i, column=1)
        ttk.Label(root, text="Label "+str(i)).grid(row=i)
    root.mainloop()


# new set up for gui

from tkinter import *
from tkinter import ttk
import sqlite3
# 
class mainBomWin:
# 
    def __init__(self, root):
        root.title("Bill of Materials")
        #  
        mainframe = ttk.Frame(root, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        #  
        self.search_text = StringVar()
        search_text_entry = ttk.Entry(mainframe, width=12, textvariable=self.search_text)
        search_text_entry.grid(column=2, row=1)
        # 
        ttk.Button(mainframe, text="Search", command=self.search_part(mainframe)).grid(column=3, row=1,sticky=W)
        # 
        for child in mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)
        # 
        # 
    def search_part(self, *args):
        
        try:
            conn = sqlite3.connect("bom.db")    
            c = conn.cursor()
            value=str(self.search_text.get())
            query = "SELECT * FROM part WHERE part=?"
            c.execute(query, (value,))
            rows = c.fetchall()
            i=0
            j=0
            for index in rows:
                j=0
                for cell in (range(len(index)-2)):
                    print(i)
                    ttk.Label(self.mainframe, text=str(index[cell])).grid(row=i+1, column=j+1, padx=4, sticky=W)
                    j+=1
                i += 1
        except ValueError:
            print('error')
            pass
root = Tk()
mainBomWin(root)
root.mainloop()
"""
# execute script example
"""
# Create and populate tables
cursor.executescript('''
CREATE TABLE Advisor(
AdvisorID INTEGER NOT NULL,
AdvisorName TEXT NOT NULL,
PRIMARY KEY(AdvisorID)
);
  
CREATE TABLE Student(
StudentID NUMERIC NOT NULL,
StudentName NUMERIC NOT NULL,
AdvisorID INTEGER,
FOREIGN KEY(AdvisorID) REFERENCES Advisor(AdvisorID),
PRIMARY KEY(StudentID)
);
  
INSERT INTO Advisor(AdvisorID, AdvisorName) VALUES
(1,"John Paul"), 
(2,"Anthony Roy"), 
(3,"Raj Shetty"),
(4,"Sam Reeds"),
(5,"Arthur Clintwood");
  
INSERT INTO Student(StudentID, StudentName, AdvisorID) VALUES
(501,"Geek1",1),
(502,"Geek2",1),
(503,"Geek3",3),
(504,"Geek4",2),
(505,"Geek5",4),
(506,"Geek6",2),
(507,"Geek7",2),
(508,"Geek8",3),
(509,"Geek9",NULL),
(510,"Geek10",1);
  
''')"""
from tkinter import *
from tkinter import ttk
import sqlite3

def search_part(*args):
        
    try:
        conn = sqlite3.connect("bom.db")    
        c = conn.cursor()
        value='%'+str(search_entry.get())+'%'
        query = """SELECT * FROM parts WHERE partName LIKE ?"""
        c.execute(query, (value,))
        rows = c.fetchall()
        i=3
        search_part = ttk.Frame(root, padding="5 5 5 5", relief='sunken')
        search_part.grid()
        for index in rows:
            j=1
            for cell in (range(len(index))):
                ttk.Label(search_part, text=str(index[cell])).grid(row=i+1, column=j+1, padx=4, sticky=W)
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
        for index in rows:
            j=1
            for cell in (range(len(index)-2)):
                ttk.Label(show, text=str(index[cell])).grid(row=i+1, column=j+1, padx=4, sticky=W)
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
        getPartIDFromIDQuery = "select partID from parts where partName=?"
        getPartIDFromIDVar = str(search_entry.get())
        c.execute(getPartIDFromIDQuery, (getPartIDFromIDVar,))
        query_result = c.fetchall()
        result = query_result[0][0]
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

# """
# >>> sql = 'select part, description, part_number FROM part inner join part_list on part.id = part_list.part_id'; 
# >>> cur.execute(sql)
# <sqlite3.Cursor object at 0x000001F80E1F5BC0>
# >>> cur.fetchall()
# [('Turntable', 'Turntable Assembly', '100AS001'), ('Turntable', 'DC202 turntable', '100AS001')]
# >>>"""

# '''
#     cur.execute("""
#     create table part (
#     id integer primary key, part text, 
#     description text, material text, 
#     part_number text, supplier text);
#     """)
# '''

# cur.executescript('''
# create table parts (
#     partID integer primary key,
#     partName text,
#     partDescription text,
#     partCost text,
#     partSupplier text,
#     partNumber text
#     );
    
# create table bomList (
#     assyId integer primary key,
#     partID integer,
#     qtyUsed integer,
#     foreign key(partID) references part(partID)
#     );
#     ''')
# cur.executescript('''
# insert into parts (partName, partDescription, partNumber)
# values 
# ('Gimbal', 'Assembly', '100AS001'),
# ('Turntable', 'Assembly', '100AS002'),
# ('Base Cover', '3d printed cover', '100PD001'),
# ('Base Plate', 'Turntable Base Plate', '100MM002'),
# ('Fiberglass screw', 'M6', '91075A101'),
# ('SS screw', '1/4-20', '91012A111'),
# ('Arm', 'Gimbal Arm', '100AS008'),
# ('Rail', 'Gimbal Rail', '100MM006');''')

# cur.executescript('''
# insert into bomList (assyId, partID, qtyUsed)
# values
# ('DC202', '2')
# );''')


# query = "select partID, partName, partDescription, partNumber, name from bomList inner join parts on bomList.parentID=parts.partID"
# value = [(28.)]

# c.execute(query, )
# result[0] = c.fetchone()
# result[1] = c.fetchone()


# searchID = 28
# partSearched = [] 
# for row in result:       
#     index = 0
#     if row[index] == searchID:
#         for line in row[0]:
#             partSearched.append(index)
#     index =+1


# for row in result:
#     index=0
#     for i in range(len(row)):
#         print(i)
    
