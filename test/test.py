import sqlite3

# con = sqlite3.connect('C:\\Users\\Jordan\Documents\\app\\database\\test\\example.db')
con = sqlite3.connect(":memory:")
cur = con.cursor()

#create table
cur.execute('''CREATE TABLE stocks
                (date text, trans text, symbol text, qty real, price real)''')


# Insert a row of data
cur.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

# Save (commit) the changes
con.commit()

for row in cur.execute('SELECT * FROM stocks ORDER BY price'):
        print('Date: ', row[0])
        print('Trans: ', row[1])
        print('Stock: ', row[2])
        print('Qty: ', row[3])
        print('Price: ', row[4])
        

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
con.close()

# Never do this -- insecure!
# symbol = 'RHAT'
# cur.execute("SELECT * FROM stocks WHERE symbol = '%s'" % symbol)

# import sqlite3

# con = sqlite3.connect(":memory:")
# cur = con.cursor()
# cur.execute("create table lang (name, first_appeared)")

# # This is the qmark style:
# cur.execute("insert into lang values (?, ?)", ("C", 1972))

# # The qmark style used with executemany():
# lang_list = [
#     ("Fortran", 1957),
#     ("Python", 1991),
#     ("Go", 2009),
# ]
# cur.executemany("insert into lang values (?, ?)", lang_list)

# # And this is the named style:
# cur.execute("select * from lang where first_appeared=:year", {"year": 1972})
# print(cur.fetchall())

# con.close()