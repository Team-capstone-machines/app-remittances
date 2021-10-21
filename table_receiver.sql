-- Create receiver table in remittances_db
CREATE TABLE IF NOT EXISTS receiver (
    id serial NOT NULL,
    name VARCHAR(120) NOT NULL,
    phone VARCHAR(40) NOT NULL,
    cash VARCHAR(100) NOT NULL,
    PRIMARY KEY (id)
);
