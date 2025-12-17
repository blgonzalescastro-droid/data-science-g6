-- sentencias sql
-- CREATE TABLE
CREATE TABLE alumno (
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    nro_documento varchar(20) NOT NULL,
    nombre VARCHAR(255) NOT NULL,
    email VARCHAR(100)
);

--ALTERAR UNA TABLA

ALTER TABLE alumno ADD COLUMN nota INT DEFAULT 0;

-- ELIMINAR UNA TABLA
DROP TABLE alumno;

CREATE TABLE empresa (
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT COMMENT 'Primary Key',
    ruc VARCHAR(11) NOT NULL,
    razon_social VARCHAR(255) NOT NULL,
    direccion TEXT
);