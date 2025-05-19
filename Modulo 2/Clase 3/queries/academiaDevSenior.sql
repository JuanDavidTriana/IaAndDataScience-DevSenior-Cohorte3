-- Crear base da datos de academiaDevSenior
CREATE DATABASE IF NOT EXISTS academiaDevSenior;

-- Usar la base de datos
USE academiaDevSenior;

-- Crear tabla de alumnos
CREATE TABLE IF NOT EXISTS alumnos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    apellido VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insertar datos en la tabla de alumnos
INSERT INTO academiaDevSenior.alumnos (nombre, apellido, email) VALUES ('Juan', 'Pérez', 'e@example.com');

-- Insertar varios alumnos a la vez
INSERT INTO academiaDevSenior.alumnos (nombre, apellido, email) VALUES 
('Ana', 'Gómez', 's@example.com'),
('Luis', 'Martínez', 'YR2t@example.com'),
('María', 'Rodríguez', 'mrodriguez@example.com'),
('Pedro', 'García', 'pgarcia@example.com'),
('Sofía', 'Sánchez', 'sofia@example.com'),
('Juan', 'López', 'juanlopez@example.com');

-- Primera consulta basica recuperando todos los alumnos
SELECT * FROM academiaDevSenior.alumnos;

-- Segunda consulta basica recuperar todos los datos de alumnos con el correo
SELECT * FROM academiaDevSenior.alumnos WHERE email = 'e@example.com';

-- Tercera consulta recuperar 
SELECT nombre, apellido, email FROM academiaDevSenior.alumnos 
WHERE email = 'e@example.com';

-- Agregar un nuevo columna la tabla de alumnos despues del la columna id
ALTER TABLE academiaDevSenior.alumnos ADD COLUMN documento VARCHAR(20) AFTER id;

-- Eliminar todos los estudiantes
DELETE FROM academiaDevSenior.alumnos;

-- Elminar la tabla de alumnos
DROP TABLE IF EXISTS academiaDevSenior.alumnos;

-- Crear la tabla de alumnos nuevamente
CREATE TABLE IF NOT EXISTS alumnos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    documento VARCHAR(20) NOT NULL UNIQUE,
    nombre VARCHAR(50) NOT NULL,
    apellido VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insertar datos en la tabla de alumnos
INSERT INTO academiaDevSenior.alumnos (documento, nombre, apellido, email) VALUES 
('12345678', 'Juan', 'Pérez', 'e@example.com'),
('22345678', 'Ana', 'Gómez', 's@example.com'),
('32345678', 'Luis', 'Martínez', 'YR2t@example.com'),
('42345678', 'María', 'Rodríguez', 'mrodriguez@example.com'),
('52345678', 'Pedro', 'García', 'pgarcia@example.com'),
('62345678', 'Sofía', 'Sánchez', 'sofia@example.com'),
('72345678', 'Juan', 'López', 'juanlopez@example.com'),
('82345678', 'Marcelo', 'González', 'mg@example.com'),
('92345678', 'Marisa', 'Díaz', 'md@example.com'),
('12345679', 'Eduardo', 'Santos', 'es@example.com');

-- Actualizar el correo de un alumno
UPDATE academiaDevSenior.alumnos
SET email = 'nuevoCorreo@example.com'
WHERE documento = '12345678';

