from tkinter import *
from tkinter import ttk
import sqlite3
import tkinter

# Function to add the new record to the database
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


# Show records, selects all columns
def query():
    global query_window
    query_window = Tk()
    query_window.geometry("1000x900")
    query_window.title("Records")
    connection = sqlite3.connect("bom.db")
    cursor = connection.cursor()
    cursor.execute("SELECT *, oid FROM part")
    records = cursor.fetchall()
    print(records)
    print_records = []
    i=0
    j=0
    for record in records:
        j=0
        for cell in (range(len(record)-2)):
            print(i)
            ttk.Label(query_window, text=str(record[cell])).grid(row=i+1, column=j+1, padx=4, sticky=W)
            j+=1
        i += 1
        # print_records += str(record[0]) + ", " + str(record[1]) + " , " + str(record[2]) + ", " + "\t" + str(record[3]) +"\n"
    # query_label = Label(query_window, text=print_records)
    # query_label.grid(row=0, column=0)

    connection.commit()
    connection.close()


def update():
    connection = sqlite3.connect("bom.db")
    cursor = connection.cursor()
    record_id = select_box.get()

    cursor.execute(
        'UPDATE part SET part=?, description=?, part_number=? WHERE oid=?',
        (item_part_editor.get(),item_description_editor.get(),item_part_number_editor.get(),record_id)
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
    record_id = select_box.get()

    cursor.execute("SELECT * FROM part WHERE oid=?",(record_id))
    records = cursor.fetchall()

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

    for record in records:
        item_part_editor.insert(0, record[0])
        item_description_editor.insert(0, record[1])
        item_part_number_editor.insert(0, record[2])
    save_btn = Button(editor, text="Save Record", command=update)
    save_btn.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=145)
    connection.commit()
    connection.close()

# Delete a record
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
# Add a record to the database
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


# Clickable button for submitting adding record
submit_btn = Button(window, text="Add Record to Database", command=submit)
submit_btn.grid(row=3, column=0, columnspan=2, pady=2)

# Clickable button for showing records
query_btn = Button(window, text="Show Records", command=query)
query_btn.grid(row=4, column=0, columnspan=2, pady=2)

# Update based on the ID specified in the 'Select ID' field
select_box=Entry(window, width=20)
select_box.grid(row=6, column=1, pady=2, sticky=W)

select_box_label = Label(window, text='Select ID ')
select_box_label.grid(row=6, column=0, pady=2, sticky=E)

# Create the button for updating records
edit_btn = Button(window, text="Update Record", command=edit)
edit_btn.grid(row=11, column=0, columnspan=2, pady=2)

# Create delete record button
delete_btn = Button(window, text="Delete Record", command=delete)
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

root = Tk()
root.title("Bill of Materials")
# Main frame window
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure