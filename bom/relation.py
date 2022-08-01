import sqlite3


def makeTable():
    # create part table
    cur.execute("""
        create table part (
        id integer primary key, name text);
        """)


    # # create component table
    # cur.execute("""
    #     create table component (
    #         id integer primary key, name text
    #     );""")


    # create mapping table
    cur.execute("""
        create table part_list (
            part_id integer,
            qty integer,
            foreign key(part_id) references part(id)
            );""")

def insertRows():
    cur.execute("""
    insert into part (name)
    values
    ('turntable')
    """)
    con.commit()


con = sqlite3.connect('bom.db')
cur = con.cursor()
cur.execute("""pragma foreign_keys = true;""")


# selet column from table
# stores the rows from the query into a list of tuples, extract them with .fetchall()
all_parts = cur.execute('select * from part')
all_part_list = cur.execute('select * from part_list')


# name = input('Name of part?:')
# query = """select * from part where name = ?"""
# result = cur.execute(query, (name,))
# """select * from SqliteDb_developers where name = ?"""
# makeTable()
# insertRows()
for row in cur.execute("""select * from part"""):
    print(row)

# cur.execute("""insert into part_list  values (1, 2);""")

choice = input('Search: ')

try:
    print('try block', choice)
    # cur.execute("""ALTER TABLE part_list ADD COLUMN name""")
except:
    print('Insert failed. Does not exist in part table maybe?')
con.commit()
