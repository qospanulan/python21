-- python21_sql_3

SELECT * FROM new_users;


-- GROUP BY ---------------------
SELECT role_name, COUNT(*), MIN(created_at), MAX(created_at) FROM new_users
GROUP BY role_name



