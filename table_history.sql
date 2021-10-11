-- Create receiver table in remittances_db
CREATE TABLE IF NOT EXISTS history (
    phone VARCHAR(20) NOT NULL,
    balance VARCHAR(20),
    date VARCHAR(20)
);