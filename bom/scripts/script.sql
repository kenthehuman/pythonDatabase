-- CREATE TABLE (
    
-- )

-- INSERT INTO part_list VALUES (

-- )

-- CREATE TABLE operations (
--     id INTEGER, description text, notes text
-- )


-- create table purchased_part ( id integer PRIMARY key, part text, description text, supplier text, cost real)

-- insert into table operations (description, notes) values ('CNC', 'Haas CNC Op')
-- insert into operations (description, notes) values ('Wiring', 'Cable and Harness Fabrication')


cur.executescript('''
create table parts (
    partID integer primary key,
    partName text,
    partDescription text,
    partCost text,
    partSupplier text,
    partNumber text
    );
    
create table bomList (
    assyId integer primary key,
    partID integer,
    qtyUsed integer,
    foreign key(partID) references parts(partID)
    );
    ''')
cur.executescript('''
insert into parts (partName, partDescription, partNumber)
values 
('Gimbal', 'Assembly', '100AS001'),
('Turntable', 'Assembly', '100AS002'),
('Base Cover', '3d printed cover', '100PD001'),
('Base Plate', 'Turntable Base Plate', '100MM002'),
('Fiberglass screw', 'M6', '91075A101'),
('SS screw', '1/4-20', '91012A111'),
('Arm', 'Gimbal Arm', '100AS008'),
('Rail', 'Gimbal Rail', '100MM006');''')

cur.executescript('''
insert into bomList (assyId, partID, qtyUsed)
values
('DC202', '2')
);''')

cur.executescript('''
insert into parts (partName, partDescription, partSupplier, partNumber)
VALUES
('DC202', 'Precision Dual-Axis Compact Positioner', 'DE', 'DC202-a'),
('Gimbal', 'Gimbal Assembly', 'DE', '100AS001'),
('Turntable', 'Turntable Assembly', 'DE', '100AS002');
''')


-- DC202 top level part
cur.executescript("""
insert into bomList (parentID, childID, qtyUsed, name) VALUES
(26, 27, 1, 'DC202'),
(26, 28, 1, 'DC202'),
(26, 8, 6, 'DC202')
""")


-- DC202 Turntable part
cur.execute("""
insert into bomList (parentID, childID, qtyUsed, name)
VALUES
(28, 1, 1, 'DC202 Turntable Assy - Baseplate'),
(28, 2, 1, 'DC202 Turntable Assy - Spacer'),
(28, 3, 1, 'DC202 Turntable Assy - Limit Switch Rod'),
(28, 4, 1, 'DC202 Turntable Assy - Turntable'),
(28, 5, 1, 'DC202 Turntable Assy - Turntable Cover'),
(28, 6, 1, 'DC202 Turntable Assy - Limit Switch Cover'),
(28, 15, 7, 'DC202 Turntable - M3x0.5x10mm FH SS Screws');
""")

-- DC202 Gimbal part
cur.execute("""
insert into bomList (parentID, childID, qtyUsed, name)
VALUES
(27, 40, 1, 'DC202 Gimbal Assy - Lower Pulley'),
(27, 30, 1, 'DC202 Gimbal Assy - Gimbal Rail'),
(27, 35, 1, 'DC202 Gimbal Assy - Roll Plate Adapter'),

""")


insert into bomList (parentID, childID, qtyUsed, name) values (26, 27, 1, 'DC202')
-- cur.execute('drop table bomList') drop table
cur.executescript('''
create table bomList (
    parentID integer,
    childID integer,
    qtyUsed integer,
    name text,
    foreign key(childID) references parts(partID)
    foreign key(parentID) references parts(partID)
    );
    ''')



-- retreive part id or name respectively
getPartNameFromIDQuery = "select partName from parts where partID=?"
getPartNameFromIDVar = 26
cur.execute(getPartNameFromIDQuery, (getPartNameFromIDVar,))
result = cur.fetchall()


getPartIDFromIDQuery = "select partID from parts where partName=?"
getPartIDFromIDVar = "DC202"
cur.execute(getPartIDFromIDQuery, (getPartIDFromIDVar,))
query_result = cur.fetchall()
result = query_result[0][0]
-- Look for all parts in bomList with the ID found
cur.execute("select childID from bomList where parentID = ?", (result,)) # childID's gets the children for ID
-- Go back thru the parts table and print out info based on the childID results

cur.executescript("""
select partName, partDescription, partNumber from parts inner join bomList on parts.partID = bomList.parentID;
""")
cur.fetchall()


cur.executescript("""
select partName from parts outer join bomList on parts.partName = bomList.name
""")
cur.fetchall()

cur.executescript("""
select partName, partDescription, partNumber from parts cross join bomList
""")
cur.fetchall()

>>> cur.execute("select * from parts where partID = 26") 
<sqlite3.Cursor object at 0x000001F827A35040>
>>> cur.fetchall()
[(26, 'DC202', 'Precision Dual-Axis Compact Positioner', None, 'DE', 'DC202-a')]
>>>