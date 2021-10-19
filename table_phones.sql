-- Create phones table in remittances_db
CREATE TABLE IF NOT EXISTS phones (
    id serial NOT NULL,
    phone VARCHAR(40) NOT NULL,
    phone_desencrypt VARCHAR(40) NOT NULL,
    PRIMARY KEY (id),
    CONSTRAINT fk_phone
        FOREIGN KEY (phone)
            REFERENCES receiver(phone)
            ON DELETE CASCADE
);
