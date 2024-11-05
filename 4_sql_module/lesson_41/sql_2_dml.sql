SELECT * FROM table_1_renamed;

SELECT id, first_name, last_name, age FROM table_1_renamed;


INSERT INTO table_1_renamed (first_name, age)
VALUES ('Aidar', 18),
	   ('Safira', 24),
	   ('Sasha', 13);


ALTER TABLE table_1_renamed
ADD last_name VARCHAR(30);


UPDATE table_1_renamed
SET last_name='test';


UPDATE table_1_renamed
SET last_name='Tlepov'
WHERE first_name='Aidar';


DELETE FROM table_1_renamed
WHERE id=3;



