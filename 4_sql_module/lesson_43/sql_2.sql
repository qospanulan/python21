-- python21_sql_3

SELECT * FROM table_1
OFFSET 3
LIMIT 5;


SELECT * FROM new_users
LIMIT 10;


-- 1 ---------------------------
SELECT * FROM new_users
ORDER BY created_at
LIMIT 5;

-- 2 ----------------------------
SELECT * FROM new_users
WHERE role_name='guest'
ORDER BY created_at DESC
LIMIT 5;

-- 3 ----------------------------
SELECT DISTINCT role_name FROM new_users;




















