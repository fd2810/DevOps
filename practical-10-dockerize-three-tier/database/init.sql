CREATE TABLE IF NOT EXISTS students (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    course VARCHAR(100) NOT NULL
);

INSERT INTO students (name, email, course)
VALUES
('Rahul', 'rahul@gmail.com', 'BCA'),
('Priya', 'priya@gmail.com', 'BSc CS'),
('Amit', 'amit@gmail.com', 'BCA');

