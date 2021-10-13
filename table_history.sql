-- Create receiver table in remittances_db
CREATE TABLE IF NOT EXISTS history (
    id serial NOT NULL PRIMARY KEY,
    date DATE DEFAULT (CURRENT_DATE),
    phone VARCHAR(40) NOT NULL,
    balance VARCHAR(100)
);
