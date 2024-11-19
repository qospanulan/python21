-- python21_sql_3

CREATE TABLE table_1 (
	id SERIAL PRIMARY KEY,
	name VARCHAR (30) NOT NULL,
	surname VARCHAR (30)
);


INSERT INTO table_1 (name, surname)
VALUES ('Ulan', 'Kospan'),
       ('Ermakhan', 'Alchurin'),
	   ('Dias', 'Zhabatov');

INSERT INTO table_1 (name, surname)
VALUES ('Ulan', 'Paul')


INSERT INTO table_1 (name, surname)
VALUES ('Ermakhan', 'test3'),
	   ('Ermakhan', 'test4');


SELECT * FROM table_1;



SELECT name, COUNT(*) as cnt_of_users, SUM(id), MAX(id), AVG(id) FROM table_1
GROUP BY name;


SELECT DISTINCT name FROM table_1;


SELECT * FROM users
OFFSET 20
LIMIT 5;




SELECT * FROM users
ORDER BY created_at ASC;  -- ASC, DESC









