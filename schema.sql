CREATE DATABASE `image` /*!40100 DEFAULT CHARACTER SET utf8 COLLATE utf8_bin */ /*!80016 DEFAULT ENCRYPTION='N' */;

-- image.`references` definition

CREATE TABLE `references` (
                              `reference_PK` int NOT NULL AUTO_INCREMENT,
                              `reference_created` datetime NOT NULL,
                              `reference_modified` datetime NOT NULL,
                              `reference_name` varchar(150) COLLATE utf8_bin NOT NULL,
                              `reference_details` text COLLATE utf8_bin NOT NULL,
                              `reference_FK_campaign_PK` int NOT NULL,
                              PRIMARY KEY (`reference_PK`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb3 COLLATE=utf8_bin;


INSERT INTO image.`references` (reference_PK, reference_created, reference_modified, reference_name, reference_details, reference_FK_campaign_PK) VALUES(1, '2021-04-21 22:45:27.0', '2021-04-21 22:45:27.0', 'Prueba1', 'Referencia de prueba 1 para entorno de desarrollo.', 1);
INSERT INTO image.`references` (reference_PK, reference_created, reference_modified, reference_name, reference_details, reference_FK_campaign_PK) VALUES(2, '2021-04-21 22:45:41.0', '2021-04-21 22:45:41.0', 'Referencia numero 2', 'Referencia de prueba 2 para entorno de desarrollo.', 1);

