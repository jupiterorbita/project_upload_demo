-- TEST script file for the dogs DB --

-- READ ALL
SELECT * FROM dogs;

-- CREATE
INSERT INTO dogs
	(name, age, breed, color)
VALUES
	('Spot', 4, 'Labrador', 'brown'),
    ('Everest', 6, 'Husky', 'black and white'),
    ('Zoey', 4, 'Beagle', 'brown');

INSERT INTO dogs
	(name, age, breed, color)
VALUES
	('Spot', 4, 'Labrador', 'brown');

-- (READ ONE) GET one dog
SELECT * FROM dogs
WHERE id = 2;


-- UPDATE one dog
UPDATE dogs
SET
	name = "Spot test",
	age = 6,
	breed = "test breed",
	color = "test color"
WHERE id = 4;
        



