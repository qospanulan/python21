

CREATE TABLE table_1 (
	id SERIAL PRIMARY KEY,
	name VARCHAR (30) NOT NULL,
	surname VARCHAR (30)
);


ALTER TABLE table_1
ADD age INTEGER;


ALTER TABLE table_1
DROP surname;


ALTER TABLE table_1
RENAME name TO first_name;


ALTER TABLE table_1
RENAME TO table_1_renamed;


-- == DROP ==========================================================================

CREATE TABLE table_to_delete (
	id SERIAL PRIMARY KEY,
	name VARCHAR (30) NOT NULL,
	surname VARCHAR (30)
);

DROP TABLE table_to_delete;

