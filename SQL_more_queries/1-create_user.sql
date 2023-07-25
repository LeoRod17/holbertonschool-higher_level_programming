-- Write a script that creates the MySQL server user user_0d_1.

CREATE LOGIN  if NOT EXISTS 'user_0d_1'@'localhost' WITH PASSWORD 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* to 'user_0d_1'@'localhost' WITH GRANT OPTION;