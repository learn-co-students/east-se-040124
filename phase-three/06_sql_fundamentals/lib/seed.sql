DELETE FROM owners;
DELETE FROM pets;
DELETE FROM appointments;
DELETE FROM procedures;


INSERT INTO owners (name, age, experience) VALUES
('Emiley', 29, 5),
('Carisa', 23, 3),
('Kailey', 23, 3);


INSERT INTO pets (name, age, breed, owner_id)
VALUES ('Apollo', 2, 'Dog', 1),
('Dayna', 3, 'Dog', 3),
('John Ham', 1, 'Hamster', 1),
('Nymeria', 1, 'Hamster', 1);


INSERT INTO procedures (name)
VALUES ('Allergy Relief'),
('Teeth cleaning');


INSERT INTO appointments (date, doctor_name, pet_id, procedure_id)
VALUES ('May 20, 2024', 'Dr. Ross', 1, 1),
('May 22, 2024', 'Dr. Bailey', 2, 1),
('April 20, 2024', 'Dr. Ross', 1, 2),
('May 20, 2024', 'Dr. Bailey', 3, 1),
('November 20, 2024', 'Dr. House', 4, 1),
('December 20, 2024', 'Dr. House', 1, 2);