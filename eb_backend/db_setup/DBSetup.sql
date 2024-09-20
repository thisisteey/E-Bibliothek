-- Prepares the PostgreSQL server for E-Bibliothek

-- Drop the database if it already exists
DROP DATABASE IF EXISTS e_bibliothek_db;

--Create the new database
CREATE DATABASE e_bibliothek_db
	WITH
	OWNER = postgres
	ENCODING = 'utf8'
	CONNECTION LIMIT = -1;

-- Add a comment on the database
COMMENT ON DATABASE e_bibliothek_db
	IS 'The database storage for E-Bibliothek';

-- Drop the role if it already exists
DROP ROLE IF EXISTS e_bibliothek_user;

-- Create the new role
CREATE ROLE e_bibliothek_user
	WITH
	LOGIN
	REPLICATION
	BYPASSRLS
	PASSWORD 'e_bibliothek_pwd';

-- Grant privileges
GRANT ALL ON DATABASE e_bibliothek_db TO e_bibliothek_user;