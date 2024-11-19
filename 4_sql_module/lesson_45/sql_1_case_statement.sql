SELECT * FROM new_users;


SELECT 
	username,
	email,
	role_name,
	created_at,
	CASE
	    WHEN role_name IN ('admin', 'moderator') THEN 'Сотрудник'
		ELSE 'Неизвестно'
	END as test
FROM new_users;


























































