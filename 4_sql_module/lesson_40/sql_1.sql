

CREATE TABLE table_2 (
	id SERIAL PRIMARY KEY,
	name VARCHAR (30) NOT NULL,
	surname VARCHAR (30)
);


INSERT INTO table_2 (name, surname)
VALUES ('Ulan', 'Kospan');


INSERT INTO table_2 (name, surname)
VALUES ('Name1', 'Surname1'),
       ('Name2', 'Surname2'),
	   ('Name3', 'Surname3');


SELECT id, name, surname FROM table_2;


SELECT * FROM table_2;






