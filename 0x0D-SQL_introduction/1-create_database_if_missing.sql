-- Write a script that creates the database hbtn_0c_0 in your MySQL server.
-- If the database hbtn_0c_0 already exists, your script should not fail.
-- You are not allowed to use the SELECT or SHOW statements.

IF NOT EXISTS (SELECT 1 FROM information_schema.schemata WHERE schema_name = 'hbtn_0c_0') THEN
    CREATE DATABASE hbtn_0c_0;
END IF;
