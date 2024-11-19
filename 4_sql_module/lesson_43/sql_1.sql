-- python21_sql_3

SELECT * FROM table_1;

INSERT INTO table_1 (surname, name) 
VALUES ('surname1', 'name1');

INSERT INTO table_1 (surname, name) 
VALUES ('surname2', 'name2'),
       ('surname3', 'name3');





SELECT 
    name as "first name",
	surname as "last name"
FROM table_1
WHERE "name"='Ermakhan';




UPDATE table_1
SET surname='Kerei'
WHERE surname='test1';


























