"""
To extract parts and stuff from excel sheet and add it into a database
This script extracts from the DC202 BOM made 7/14/2022, to add some purchased parts to the database.
By:Ken
Date:8/1/2022
"""
from openpyxl import load_workbook
from classes import DEpart
from mapping import NAME, DESCRIPTION, PART_NUMBER, SUPPLIER

import sqlite3

workbook = load_workbook("BOM_Sample.xlsx")
sheet = workbook.active

hardware = []

# for value in sheet.iter_rows(min_row=10,
#                             max_row=10,
#                             min_col=2,
#                             max_col=6,
#                             values_only=True):
#     print(value)
# 

for row in sheet.iter_rows(min_row=10,
                            max_row=10,
                            values_only=True):
    product = DEpart(name=row[NAME],
                    description=row[DESCRIPTION],
                    part_number=row[PART_NUMBER],
                    supplier=row[SUPPLIER])
    hardware.append(product)

# convert list to a list of tuple to insert with .execute method
hardware = [tuple(hardware)]

# gets the description of the first thing
# hardware[0][0].description
# hardware[0][0].name
# hardware[0][0].part_number
# hardware[0][0].supplier

con = sqlite3.connect("bom.db")
cur = con.cursor()

cur.execute()

cur.execute("""insert into part 
            (part, description, part_number, supplier) values (?, ?, ?), 
            ((hardware[0].description,), (hardware[0].name,), 
            (hardware[0].part_number,), (hardware[0].supplier,))""")


# gets from rows noted and loads into hardware
for row in sheet.iter_rows(min_row=13,
                            max_row=31,
                            values_only=True):
    product = DEpart(name=row[NAME],
                    description=row[DESCRIPTION],
                    part_number=row[PART_NUMBER],
                    supplier=row[SUPPLIER])
    hardware.append(product)
# puts multiple variables into a query for inserting
for i in range(len(hardware)):        
    part = hardware[i].name
    description = hardware[i].description
    part_number = hardware[i].part_number
    description = hardware[i].description
    query_variable = [(part), (description), (part_number), (description)]
    cur.execute(query, query_variable)
query = """insert into part 
            (part, description, part_number, supplier) values (?, ?, ?, ?)"""
query_variable = [(part), (description), (part_number), (description)]
cur.execute(query, query_variable)
