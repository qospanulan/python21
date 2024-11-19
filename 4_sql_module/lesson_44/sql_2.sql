-- python21_sql_4

CREATE table table_2 (
  id SERIAL PRIMARY KEY,
  first_name VARCHAR(30),
  last_name VARCHAR(30),
  age INTEGER
);

INSERT INTO table_2 (first_name, last_name, age)
VALUES ('first name 1', 'last name 1', 18),
       ('Dana', 'Kapysh', 21),
	   ('Margo', 'Kospan', 25);

INSERT INTO table_2 (first_name, age)
VALUES ('first name 2', 18),
       ('Kainar', 21),
	   ('Milan', 25);


INSERT INTO table_2 (first_name)
VALUES ('first name 3'),
       ('Daniel'),
	   ('Davlat');


SELECT id, first_name, coalesce(last_name, 'surname placeholder'), age FROM table_2;


SELECT * FROM table_2
ORDER BY age DESC NULLS LAST;




