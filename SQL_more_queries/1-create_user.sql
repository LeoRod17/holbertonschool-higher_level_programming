-- Write a script that creates the MySQL server user user_0d_1.

CREATE USER  if not EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

GRANT ALL PRIVILEGES ON *.* to 'user_0d_1'@'localhost';