
DROP TABLE IF EXISTS driver;
DROP TABLE IF EXISTS country;
DROP TABLE IF EXISTS session;

CREATE TABLE driver (
    driver_number INTEGER,
    name_acronym TEXT,
    full_name TEXT,
    PRIMARY KEY (driver_number, name_acronym)
);


CREATE TABLE country (
    country_key INTEGER PRIMARY KEY,
    country_name TEXT
);

CREATE TABLE session (
    session_key INTEGER PRIMARY KEY,
    country_key INTEGER,
    'year' INTEGER,
    date_start TEXT,
    date_end TEXT,
    FOREIGN KEY (country_key) REFERENCES country(country_key)
);
