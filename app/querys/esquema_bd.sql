--
-- Database: foundanies
--
DROP DATABASE IF EXISTS foundanies;
CREATE SCHEMA foundanies;
USE foundanies;


CREATE TABLE usuario (
  usuario_id int(11) AUTO_INCREMENT NOT NULL,
  usuario_login varchar(100) NOT NULL,
  usuario_senha varchar(50),
  usuario_logado int(11) NOT NULL DEFAULT '0',
  usuario_email varchar(100) NOT NULL,
  usuario_caminho_foto varchar(100) NOT NULL DEFAULT 'user_profile.jpg',
  PRIMARY KEY (usuario_id)
  
);


