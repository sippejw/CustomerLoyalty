DROP TABLE IF EXISTS customers;

CREATE TABLE customers (
	phone_number TEXT PRIMARY KEY,
	joined TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	first_name TEXT,
	last_name TEXT,
	email_address TEXT,
	num_visits INTEGER NOT NULL
);
