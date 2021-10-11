-- Create receiver table in remittances_db
CREATE TABLE IF NOT EXISTS receiver (
    name VARCHAR(120) NOT NULL,
    phone VARCHAR(10) NOT NULL,
    cash VARCHAR(100) NOT NULL
);
