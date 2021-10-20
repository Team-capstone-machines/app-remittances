-- Create receiver table in remittances_db
CREATE TABLE IF NOT EXISTS history (
    id serial NOT NULL,
    date TIMESTAMP default (localtimestamp(0)),
    phone VARCHAR(40) NOT NULL,
    balance VARCHAR(100),
    PRIMARY KEY (id)
);
