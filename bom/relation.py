import sqlite3


def makeTable():
    # create part table
    # cur.execute("""
    #     create table part (
    #     id integer primary key, name text);
    #     """)
    cur.execute("""
    create table part (
    id integer primary key, part text, 
    description text, material text, 
    part_number text, supplier text);
    """)

# component text, description text, material text, part_number text, supplier text
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


# # selet column from table
# # stores the rows from the query into a list of tuples, extract them with .fetchall()
# all_parts = cur.execute('select * from part')
# all_part_list = cur.execute('select * from part_list')


# # name = input('Name of part?:')
# # query = """select * from part where name = ?"""
# # result = cur.execute(query, (name,))
# # """select * from SqliteDb_developers where name = ?"""
# # makeTable()
# # insertRows()
# for row in cur.execute("""select * from part"""):
#     print(row)

# # cur.execute("""insert into part_list  values (1, 2);""")

# choice = input('Search: ')

# try:
#     print('try block', choice)
#     # cur.execute("""ALTER TABLE part_list ADD COLUMN name""")
# except:
#     print('Insert failed. Does not exist in part table maybe?')
# con.commit()

a= cur.execute("select * from part where name = 'turntable'")

# multiple records as once
# make list of tuples
recordsToInsert = [('Turntable', 'Turntable Assembly', '100AS001'),
                    ('Base', 'Base Assembly', '100AS002')]

query_insert = """INSERT INTO part (part, description, part_number)
                    values (?, ?, ?);"""

cur.executemany(query_insert, recordsToInsert)


# insert one record
cur.execute("insert into part (name) values ('arm')")

# get id from part for when you are adding for part_list bom thing
a = cur.execute("select id from part where name ='base'") # once fetched it is gone from cur object

a.fetchall()
[(5,)]


query = input('Search what?')
result = cur.execute("SELECT * FROM part where name=?", [query]).fetchall()

cur.execute("insert into part (part, description, part_number) values ('DC202', 'Dual Axis Compact Positioner', 'DC202')")

