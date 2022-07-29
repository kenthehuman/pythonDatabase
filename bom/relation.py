import sqlite3

con = sqlite3.connect('bom.db')
cur = con.cursor()

# create part table
cur.execute("""
     create table part (
     id integer primary key autoincrement, name text);
     """)


 # create component table
cur.execute("""
     create table component (
         id integer primary key autoincrement, name text
     );""")


# create mapping table
cur.execute("""
    create table part_component (
        component_id integer,
        part_id integer,
        foreign key(component_id) references child(id),
        foreign key(part_id) references part(id)
        );""")