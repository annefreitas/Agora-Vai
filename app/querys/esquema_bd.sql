--
-- Database: foundanies
--
DROP DATABASE IF EXISTS foundnaies;
CREATE SCHEMA foundanies;
USE foundanies;


-- Estrutura da tabela usuario
--

DROP TABLE IF EXISTS usuario;
CREATE TABLE usuario (
  usuario_id int(11) AUTO_INCREMENT NOT NULL,
  usuario_login varchar(100) NOT NULL,
  usuario_senha varchar(50),
  usuario_email varchar(100) NOT NULL,
  usuario_status int(11) NOT NULL DEFAULT '0',
  usuario_caminho_foto varchar(100),
  usuario_descricao varchar(140) NOT NULL,
  PRIMARY KEY (usuario_id)
);

