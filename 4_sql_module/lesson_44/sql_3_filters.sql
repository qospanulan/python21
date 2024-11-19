-- python21_sql_4

SELECT * FROM new_users
WHERE role_name='admin';


SELECT * FROM new_users
WHERE role_name='admin' OR role_name='guest';


SELECT * FROM new_users
WHERE username LIKE '%s%';


SELECT * FROM new_users
WHERE username LIKE '__t%';

SELECT * FROM new_users
WHERE username LIKE '%o_';



SELECT * FROM new_users
WHERE created_at >= '2023-01-01' AND created_at < '2024-01-01'
ORDER BY created_at;


SELECT * FROM new_users
WHERE created_at BETWEEN '2023-01-01' AND '2024-01-01'
ORDER BY created_at;


SELECT * FROM new_users
WHERE role_name IN ('admin', 'guest', 'moderator');


SELECT * FROM new_users
WHERE role_name='admin' OR role_name='guest' OR role_name='moderator';


SELECT * FROM new_users
WHERE NOT role_name='admin';

SELECT * FROM new_users
WHERE role_name!='admin';



SELECT * FROM new_users
WHERE NOT (role_name='admin' OR role_name='guest' OR role_name='moderator');

SELECT * FROM new_users
WHERE role_name!='admin' AND role_name!='guest' AND role_name!='moderator';

-- не правильно ----------------------------------------------------------
SELECT * FROM new_users
WHERE NOT role_name='admin' OR role_name='guest' OR role_name='moderator';



