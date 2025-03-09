DROP TABLE userdata;

CREATE TABLE IF NOT EXISTS userdata (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    system_name varchar(255),
    jsondata JSON,
    squadron VARCHAR(255),
    station_type VARCHAR(255)
)