DROP TABLE IF EXISTS appointments;

CREATE TABLE IF NOT EXISTS appointments(
    id INTEGER PRIMARY KEY,
    date TEXT,
    doctor_name TEXT,
    pet_id INTEGER,
    procedure_id INTEGER
);

INSERT INTO appointments (date, doctor_name, pet_id, procedure_id)
VALUES ('May 20, 2024', 'Dr. Ross', 1, 1),
('May 22, 2024', 'Dr. Bailey', 2, 1),
('April 20, 2024', 'Dr. Ross', 1, 2),
('May 20, 2024', 'Dr. Bailey', 3, 1),
('November 20, 2024', 'Dr. House', 4, 1),
('December 20, 2024', 'Dr. House', 1, 2);