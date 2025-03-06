DROP DATABASE IF EXISTS hbtn_0e_0_usa;
CREATE DATABASE hbtn_0e_0_usa;
USE hbtn_0e_0_usa;

CREATE TABLE IF NOT EXISTS states (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);

DELETE FROM states;
ALTER TABLE states AUTO_INCREMENT = 1;

INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");
