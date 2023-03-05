CREATE DATABASE foxford_db;
CREATE USER fox_admin WITH PASSWORD '1234';
ALTER ROLE booking_admin SET client_encoding TO 'utf8';
ALTER ROLE booking_admin SET default_transaction_isolation TO 'read committed';
ALTER ROLE booking_admin SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE foxford_db TO fox_admin;