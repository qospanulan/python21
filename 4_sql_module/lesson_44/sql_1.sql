-- python21_sql_4

CREATE table table_1 (
  col1 NUMERIC(10, 2)
);

INSERT INTO table_1 (col1)
VALUES (1.22),
       (2.43),
	   (1.99);

SELECT col1, cast(col1 as INTEGER) FROM table_1;

--------------------------------------------------------------
--------------------------------------------------------------

SELECT id, username, created_at FROM new_users;


SELECT 
	id, 
	username, 
	created_at,
	cast(created_at as VARCHAR) as created_at_2,
	created_at::VARCHAR(30) as created_at_3
FROM new_users;

