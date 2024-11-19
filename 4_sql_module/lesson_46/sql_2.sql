ALTER TABLE department 
ADD city VARCHAR(30);

CREATE TABLE employees (
    id SERIAL PRIMARY KEY,
	first_name VARCHAR(30),
	last_name VARCHAR(30),
	salary INTEGER,
	city VARCHAR(30),
	department_id INTEGER REFERENCES department(id) ON DELETE SET NULL
);

SELECT * FROM department;
SELECT * FROM employees;

INSERT INTO department (name, description)
VALUES ('IT', 'IT department');

INSERT INTO department (name, description)
VALUES ('QA', 'QA department');

INSERT INTO employees (first_name, last_name, department_id, salary, city)
VALUES ('Ulan', 'test1', 5, 2200, 'Aqtobe'),
       ('Kanat', 'test2', 4, 1200, 'Almaty'),
	   ('Egor', 'test3', 3, 1000, 'Almaty'),
	   ('Sasha', 'test4', 4, 3000, 'Aqtobe'),
	   ('Katya', 'test5', 5, 2500, 'Astana');



SELECT * FROM department;


UPDATE department
SET city='Aqtobe'
WHERE id=5;

UPDATE department
SET city='Astana'
WHERE id=3;

UPDATE department
SET city='Almaty'
WHERE id=4;

UPDATE department
SET city='Aqtau'
WHERE id=6;





SELECT *
FROM department as d
INNER JOIN employees as e
ON d.city=e.city


SELECT *
FROM department as d
LEFT JOIN employees as e
ON d.city=e.city















