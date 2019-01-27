CREATE TABLE holiday (
id int AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(256) NOT NULL,
celebrated_on date NOT NULL,
message varchar(256) NOT NULL);

INSERT INTO holiday
(name, celebrated_on, message)
VALUES('Dia de los heroes de la patria', '2019-03-01', 'Feliz dia de los heroes de la patria');

/* SEMANA SANTA */
INSERT INTO holiday
(name, celebrated_on, message)
VALUES('Jueves Santo', '2019-04-18', 'Muchas bendiciones en este jueves santo');

INSERT INTO holiday
(name, celebrated_on, message)
VALUES('Viernes Santo', '2019-04-19', 'Muchas bendiciones en este viernes santo');

INSERT INTO holiday
(name, celebrated_on, message)
VALUES('Pascuas', '2019-04-21', 'Felices pascuas');

/*---------------------------------------------------------------*/

INSERT INTO holiday
(name, celebrated_on, message)
VALUES('Dia del trabajador', '2019-05-01', 'Feliz dia del trabajador');

INSERT INTO holiday
(name, celebrated_on, message)
VALUES('Dia de de la independecia', '2019-05-14', 'Feliz dia de la independecia');

INSERT INTO holiday
(name, celebrated_on, message)
VALUES('Dia de de la independecia y Dia de la madre', '2019-05-15', 'Feliz dia a todas las madres!');

INSERT INTO holiday
(name, celebrated_on, message)
VALUES('Dia de de la paz del chaco', '2019-06-12', 'Feliz dia de la paz del chaco');

INSERT INTO holiday
(name, celebrated_on, message)
VALUES('Fundacion de Asuncion', '2019-08-15', 'Feliz dia de la fundacion de asuncion');

INSERT INTO holiday
(name, celebrated_on, message)
VALUES('Victoria de boqueron', '2019-09-29', 'Feliz dia de la victoria de Boqueron');

INSERT INTO holiday
(name, celebrated_on, message)
VALUES('Dia de la virgen de Caacupe', '2019-12-08', 'Feliz dia de la virgen de Caacupe');

INSERT INTO holiday
(name, celebrated_on, message)
VALUES('Navidad', '2019-12-25', 'Feliz navidad a todos!');

INSERT INTO holiday
(name, celebrated_on, message)
VALUES('Año nuevo', '2020-01-01', 'Feliz año nuevo');