CREATE TABLE (
    
)

INSERT INTO part_list VALUES (

)

CREATE TABLE operations (
    id INTEGER, description text, notes text
)


create table purchased_part ( id integer PRIMARY key, part text, description text, supplier text, cost real)

insert into table operations (description, notes) values ('CNC', 'Haas CNC Op')
insert into operations (description, notes) values ('Wiring', 'Cable and Harness Fabrication')