create database projetoweb;
use projetoweb;

CREATE TABLE `jogos` (
  `id_concurso` int(11) NOT NULL AUTO_INCREMENT,
  `dezena_1` tinyint(4) NOT NULL,
  `dezena_2` tinyint(4) NOT NULL,
  `dezena_3` tinyint(4) NOT NULL,
  `dezena_4` tinyint(4) NOT NULL,
  `dezena_5` tinyint(4) NOT NULL,
  `dezena_6` tinyint(4) NOT NULL,
  `dezena_7` tinyint(4) NOT NULL,
  `dezena_8` tinyint(4) NOT NULL,
  `dezena_9` tinyint(4) NOT NULL,
  `dezena_10` tinyint(4) NOT NULL,
  `dezena_11` tinyint(4) NOT NULL,
  `dezena_12` tinyint(4) NOT NULL,
  `dezena_13` tinyint(4) NOT NULL,
  `dezena_14` tinyint(4) NOT NULL,
  `dezena_15` tinyint(4) NOT NULL,
  PRIMARY KEY (`id_concurso`)
) ENGINE=InnoDB AUTO_INCREMENT=2028 DEFAULT CHARSET=latin1