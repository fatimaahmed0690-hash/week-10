CREATE DATABASE IF NOT EXISTS cyber_platform;
USE cyber_platform;

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE,
    password_hash VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS incidents (
    id INT AUTO_INCREMENT PRIMARY KEY,
    category VARCHAR(100),
    severity VARCHAR(50),
    status VARCHAR(50),
    description TEXT,
    incident_date DATE
);

INSERT INTO users (username, password_hash)
VALUES ('admin', SHA2('admin123',256));

INSERT INTO incidents (category,severity,status,description,incident_date)
VALUES
('Malware','High','Open','Ransomware detected','2025-01-01');
