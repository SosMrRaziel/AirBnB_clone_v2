CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hhnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hhnb_dev'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'hhnb_dev'@'localhost';
FLUSH PRIVILEGES;