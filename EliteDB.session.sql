CREATE TABLE IF NOT EXISTS userdata (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    system_name varchar(255),
    jsondata JSON
)