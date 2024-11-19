CREATE TABLE department (
	id SERIAL PRIMARY KEY,
	name VARCHAR(30),
	description TEXT
);

CREATE TABLE employees (
    id SERIAL PRIMARY KEY,
	first_name VARCHAR(30),
	last_name VARCHAR(30),
	department_id INTEGER
);


INSERT INTO department (name, description)
VALUES ('IT', 'IT department'),
	   ('HR', 'HR department'),
	   ('Sales', 'Sales department');


INSERT INTO employees (first_name, last_name, department_id)
VALUES ('Ulan', 'test1', 1),
       ('Kanat', 'test2', 2),
	   ('Egor', 'test3', 3);


SELECT * FROM department;

SELECT * FROM employees;


SELECT e.*, d.name FROM employees as e, department as d
WHERE e.department_id=d.id;




INSERT INTO employees (first_name, last_name, department_id)
VALUES ('Potter', 'test7', 7);















