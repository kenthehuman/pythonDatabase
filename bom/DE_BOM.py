""" 
by Ken Durlin
Stores parts bill of materials.
"""
import sqlite3

# Create connection to database
sqliteConnection = sqlite3.Connection('C:\\Users\\Jordan\Documents\\app\\database\\bom\\DE_bom.db')

# Create curos for executin queries.
sqliteCursor = sqliteConnection.cursor()
print('Database connection initiated.')

sqliteCursor.execute('''CREATE TABLE parts
                        ())