CREATE TABLE IF NOT EXISTS staff(
                        id serial PRIMARY KEY,
                        name VARCHAR(255) NOT NULL,
                        contact VARCHAR(255) NOT NULL,
                        address VARCHAR(255) NOT NULL
                    );
INSERT INTO staff(name, contact, address) VALUES('SAFAL', '9849073333', 'New Baneswor')