DROP TABLE IF EXISTS bookings;
DROP TABLE IF EXISTS fitness_classes;
DROP TABLE IF EXISTS class_types;
DROP TABLE IF EXISTS members;

CREATE TABLE members(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    address TEXT,
    phone VARCHAR(255),
    email VARCHAR(255),
    premium BOOLEAN,
    membership_no INT
);

CREATE TABLE class_types(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    description TEXT,
    intensity VARCHAR(255),
    difficulty VARCHAR(255)
);

CREATE TABLE fitness_classes(
    id SERIAL PRIMARY KEY,
    class_type_id INT REFERENCES class_types(id) ON DELETE CASCADE,
    date VARCHAR(255),
    time VARCHAR(255),
    duration VARCHAR(255),
    instructor VARCHAR(255),
    capacity INT,
    location VARCHAR(255)
);

CREATE TABLE bookings(
    id SERIAL PRIMARY KEY,
    member_id INT REFERENCES members(id) ON DELETE CASCADE,
    fitness_class_id INT REFERENCES fitness_classes(id) ON DELETE CASCADE
);