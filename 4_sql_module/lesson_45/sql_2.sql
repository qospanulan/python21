CREATE TABLE students (
    id SERIAL PRIMARY KEY,
	name VARCHAR(30),
	age INTEGER
);


INSERT INTO students (name, age)
VALUES ('Asylzhan', 13),
	   ('Erkhan', 18),
	   ('Justcode', 25),
	   ('Leonid', 30),
	   ('Sasha', 8),
	   ('Dias', 14),
	   ('Erkin', 20);


SELECT * FROM students;

-- CASE STATEMENT - 0-16 Ребенок
--                  16-21 Подросток
--                  21-   Взрослый

SELECT
	name,
	age,
	CASE
		WHEN age <= 16 THEN 'Ребёнок'
		WHEN age <= 21 THEN 'Подросток'
		ELSE 'Взрослый'
	END as status
FROM students;




SELECT 
    role_name, 
	COUNT(*), 
	-- array_agg(username) 
	string_agg(username, ', ')
FROM new_users
GROUP BY role_name;




SELECT 
    role_name,
	COUNT(*) as total,
	COUNT(*) FILTER (WHERE created_at BETWEEN '2020-01-01' AND '2021-01-01') as year_2020,
	COUNT(*) FILTER (WHERE created_at BETWEEN '2021-01-01' AND '2022-01-01') as year_2021,
	COUNT(*) FILTER (WHERE created_at BETWEEN '2022-01-01' AND '2023-01-01') as year_2022,
	COUNT(*) FILTER (WHERE created_at BETWEEN '2023-01-01' AND '2024-01-01') as year_2023,
	COUNT(*) FILTER (WHERE created_at BETWEEN '2024-01-01' AND '2025-01-01') as year_2024
FROM new_users
GROUP BY role_name;




SELECT 
    role_name, 
	COUNT(*)
FROM new_users
WHERE created_at BETWEEN '2020-01-01' AND '2021-01-01'
GROUP BY role_name;



























































