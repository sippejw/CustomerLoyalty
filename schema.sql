DROP TABLE IF EXISTS customers;

CREATE TABLE customers (
	first_name TEXT,
	last_name TEXT,
	email_address TEXT,
	phone_number TEXT PRIMARY KEY,
	joined TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	num_visits INTEGER NOT NULL DEFAULT 0,
	increments_five INTEGER NOT NULL DEFAULT 0
);
