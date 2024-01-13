--check is the database exist
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- check if the user exist
CREATE USER IF NOT EXISTS 'hhnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- grant select previleges 
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hhnb_dev'@'localhost';
-- select PRIVILEGES
GRANT SELECT ON `performance_schema`.* TO 'hhnb_dev'@'localhost';
--apply changes
FLUSH PRIVILEGES;