CREATE DATABASE IF NOT EXISTS `holiday`;
USE `holiday`;

--
--  TABLE holiday
--

DROP TABLE IF EXISTS `holiday`;

CREATE TABLE `holiday` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `message` varchar(255) NOT NULL,
  `day` int(11) NOT NULL,
  `month` int(11) NOT NULL,
  PRIMARY KEY (`id`)
);

INSERT INTO `holiday` VALUES
(1,     'Día de los heroes de la patria',               'Feliz día a los heroes de la patria'           ,1,     3),
(2,     'Jueves Santo',                                 'Muchas bendiciones en este jueves santo'       ,0,     0),
(3,     'Viernes Santo',                                'Muchas bendiciones en este viernes santo'      ,0,     0),
(4,     'Pascuas',                                      '¡Felices pascuas!'                             ,0,     0),
(5,     'Día del trabajador',                           '¡Feliz día del trabajador!'                    ,1,     5),
(6,     'Día de de la independecia',                    '¡Feliz día de la independecia!'                ,14,    5),
(7,     'Día de de la independecia y Dia de la madre',  '¡Feliz día a todas las madres!'                ,15,    5),
(8,     'Día de de la paz del chaco',                   '¡Feliz día de la paz del chaco!'               ,12,    6),
(9,     'Fundación de Asunción',                        '¡Feliz día de la fundacion de Asunción!'       ,15,    8),
(10,    'Victoria de Boquerón',                         '¡Feliz día de la victoria de Boquerón!'        ,29,    9),
(11,    'Día de la Virgen de Caacupé',                  '¡Feliz día de la Virgen de Caacupé!'           ,8,     12),
(12,    'Navidad',                                      '¡Feliz navidad a todos!'                       ,25,    12),
(13,    'Año nuevo',                                    '¡Feliz año nuevo!'                             ,1,     1);

--
-- TABLE holiday_celebration_date
--

DROP TABLE IF EXISTS `holiday_celebration_date`;

CREATE TABLE `holiday_celebration_date` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `holiday_id` int(11) NOT NULL,
  `day` int(11) NOT NULL,
  `month` int(11) NOT NULL,
  `year` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `holiday_celebration_date_fk` (`holiday_id`),
  CONSTRAINT `holiday_celebration_date_fk` FOREIGN KEY (`holiday_id`) REFERENCES `holiday` (`id`)
);

--
-- 2019
--
INSERT INTO `holiday_celebration_date` VALUES
(8,1,4,3,2019),
(9,8,17,6,2019),
(10,2,18,4,2019),
(11,3,19,4,2019),
(15,4,21,4,2019);

--
-- 2020
--
INSERT INTO `holiday_celebration_date` VALUES
(12,2,9,4,2020),
(13,3,10,4,2020),
(14,4,12,4,2020);

INSERT INTO holiday_celebration_date(holiday_id, day, month, year) values (8, 15, 6, 2020);
INSERT INTO holiday_celebration_date(holiday_id, day, month, year) values (10, 28, 9, 2020);
