-- Create the Vending Service database if it doesn't exist
CREATE DATABASE IF NOT EXISTS vending_service;

-- Switch to the Vending Service database
USE vending_service;

-- Create a table to store information about medicines
CREATE TABLE IF NOT EXISTS medicines (
    medicine_id INT AUTO_INCREMENT PRIMARY KEY,
    medicine_name VARCHAR(255) NOT NULL,
    quantity INT NOT NULL,
    expiry_date DATE NOT NULL
);
-- Switch to the Vending Service database

-- Create a table to store information about workers
CREATE TABLE IF NOT EXISTS workers (
    worker_id INT AUTO_INCREMENT PRIMARY KEY,
    worker_name VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
);
use vending_service;
-- Insert a new medicine into the medicines table
INSERT INTO medicines (medicine_name, quantity, expiry_date)
VALUES ('Medicine A', 50, '2023-12-31');

-- Insert another medicine
INSERT INTO medicines (medicine_name, quantity, expiry_date)
VALUES ('Medicine B', 30, '2023-11-15');

INSERT INTO workers (worker_name,password)
values ('Prabha',18);
SELECT *FROM medicines;
DELETE FROM medicines WHERE medicine_id= 6;



