""" 
by Ken Durlin
Stores parts bill of materials.
"""
import sqlite3

def dbArchive():
    from datetime import date, datetime
    import shutil

    today = datetime.now().strftime("%d-%m-%Y_%H%M%S")
    # date.
    db_current_file = 'C:\\Users\\Jordan\\Documents\\app\\database\\bom\\DE_BOM.py'
    db_archive_dir = f'C:\\Users\\Jordan\\Documents\\app\\database\\bom\\Archive\\DE_BOM_{today}.py' 
    shutil.copyfile(db_current_file, db_archive_dir)
    
# Create Database Table 
# 'C:\\Users\\Jordan\Documents\\app\\database\\bom\\DE_bom.db'
def createTable(cur):
    #create table
    cur.execute('''CREATE TABLE stocks
                    (date text, trans text, symbol text, qty real, price real)''')

def printTable():
    for row in sqliteCursor.execute('SELECT * FROM stocks ORDER BY price'):
        print('Date: ', row[0])
        print('Trans: ', row[1])
        print('Stock: ', row[2])
        print('Qty: ', row[3])
        print('Price: ', row[4])

# sqliteCursor.execute('''CREATE TABLE parts
#                         ())

try:
    
    # Connect to DB and create a cursor
    sqliteConnection = sqlite3.connect('sql.db')
    sqliteCursor = sqliteConnection.cursor()
    print('Database connection initiated')
  
    # Write a query and execute it with cursor
    query = 'SELECT sqlite_version();'
    sqliteCursor.execute(query)
  
    # Fetch and output result
    result = sqliteCursor.fetchall()
    print('SQLite Version is {}'.format(result))

    # createTable(sqliteCursor)
    # Insert a row of data
    # sqliteCursor.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")
    # sqliteConnection.commit()
    # sqliteCursor.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")
    dbArchive()
    printTable()
  
    # Close the cursor
    sqliteCursor.close()
  
# Handle errors
except sqlite3.Error as error:
    print('Error occured - ', error)
  
# Close DB Connection irrespective of success
# or failure
finally:
    
    if sqliteConnection:
        sqliteConnection.close()
        print('SQLite Connection closed')