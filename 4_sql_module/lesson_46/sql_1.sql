CREATE TABLE department (
	id SERIAL PRIMARY KEY,
	name VARCHAR(30),
	description TEXT
);


-- ON DELETE CASCADE ===========================================================================================================

CREATE TABLE employees_1 (
    id SERIAL PRIMARY KEY,
	first_name VARCHAR(30),
	last_name VARCHAR(30),
	department_id INTEGER REFERENCES department(id) ON DELETE CASCADE
);

INSERT INTO department (name, description)
VALUES ('IT', 'IT department'),
	   ('HR', 'HR department'),
	   ('Sales', 'Sales department');


INSERT INTO employees_1 (first_name, last_name, department_id)
VALUES ('Ulan', 'test1', 1),
       ('Kanat', 'test2', 2),
	   ('Egor', 'test3', 3),
	   ('Sasha', 'test4', 2),
	   ('Katya', 'test5', 1);


SELECT * FROM department;
SELECT * FROM employees_1;


DELETE FROM department
WHERE id=2;


-- ON DELETE SET NULL ===========================================================================================================

CREATE TABLE employees_2 (
    id SERIAL PRIMARY KEY,
	first_name VARCHAR(30),
	last_name VARCHAR(30),
	department_id INTEGER REFERENCES department(id) ON DELETE SET NULL
);

SELECT * FROM department;
SELECT * FROM employees_2;

INSERT INTO department (name, description)
VALUES ('HR', 'HR department');


INSERT INTO employees_2 (first_name, last_name, department_id)
VALUES ('Ulan', 'test1', 1),
       ('Kanat', 'test2', 4),
	   ('Egor', 'test3', 3),
	   ('Sasha', 'test4', 4),
	   ('Katya', 'test5', 1);


DELETE FROM department
WHERE id=1;



