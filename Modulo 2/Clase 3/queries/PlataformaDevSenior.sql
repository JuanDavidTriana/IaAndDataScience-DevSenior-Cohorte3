-- Crear nuestra base de datos
CREATE DATABASE IF NOT EXISTS academia;

-- Usar la base de datos
USE academia;

-- Crear la tabla de estudiantes
CREATE TABLE IF NOT EXISTS estudiantes (
    id_estudiante bigint AUTO_INCREMENT PRIMARY KEY,
    numero_documento VARCHAR(20) NOT NULL UNIQUE,
    nombre VARCHAR(255) NOT NULL,
    apellido VARCHAR(255) NOT NULL,
    fecha_nacimiento DATE NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    telefono VARCHAR(20) NOT NULL
);

-- Crear la talba de docentes
CREATE TABLE IF NOT EXISTS docentes (
    id_docente bigint AUTO_INCREMENT PRIMARY KEY,
    numero_documento VARCHAR(20) NOT NULL UNIQUE,
    nombre VARCHAR(255) NOT NULL,
    apellido VARCHAR(255) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    telefono VARCHAR(20) NOT NULL,
    especialidad VARCHAR(100) NOT NULL
);

-- Crear la tabla de cursos
CREATE TABLE IF NOT EXISTS cursos (
    id_curso bigint AUTO_INCREMENT PRIMARY KEY,
    nombre_curso VARCHAR(255) NOT NULL,
    descripcion TEXT NOT NULL,
    creditos INT NOT NULL,
    id_docente bigint NOT NULL,
    FOREIGN KEY (id_docente) REFERENCES docentes(id_docente)
);

-- Crear la tabla de inscripciones
CREATE TABLE IF NOT EXISTS inscripciones (
    id_inscripcion bigint AUTO_INCREMENT PRIMARY KEY,
    id_estudiante bigint NOT NULL,
    id_curso bigint NOT NULL,
    fecha_inscripcion DATE NOT NULL,
    FOREIGN KEY (id_estudiante) REFERENCES estudiantes(id_estudiante),
    FOREIGN KEY (id_curso) REFERENCES cursos(id_curso)
);

INSERT INTO docentes (numero_documento, nombre, apellido, email, telefono, especialidad)
VALUES ('123456789', 'Juan', 'Pérez', 'e@example.com', '1234567890', 'Matemáticas'),
       ('987654321', 'María', 'Gómez', 's@example.com', '9876543210', 'Física'),
       ('456789123', 'Carlos', 'López', 'tJYwD@example.com', '4567891230', 'Química'),
       ('321654987', 'Ana', 'Martínez', '   @example.com', '3216549870', 'Biología'),
       ('654321789', 'Luis', 'Hernández', '@example.com', '6543217890', 'Programación');

INSERT INTO cursos (nombre_curso, descripcion, creditos, id_docente)
VALUES ('Matemáticas Avanzadas', 'Curso avanzado de matemáticas', 4, 1),
       ('Física Moderna', 'Curso de física moderna', 3, 2),
       ('Química Orgánica', 'Curso de química orgánica', 4, 3),
       ('Biología Celular', 'Curso de biología celular', 3, 4),
       ('Programación Web', 'Curso de programación web', 4, 5);

INSERT INTO inscripciones (id_estudiante, id_curso, fecha_inscripcion)
VALUES (1, 1, '2023-01-01'),
       (1, 2, '2023-01-02'),
       (2, 1, '2023-01-03'),
       (2, 3, '2023-01-04'),
       (3, 4, '2023-01-05'),
       (4, 5, '2023-01-06');

SELECT * FROM estudiantes;

SELECT nombre, apellido, fecha_nacimiento FROM estudiantes;

SELECT * FROM cursos WHERE creditos > 3;

SELECT c.nombre_curso, d.nombre AS nombre_docente, d.apellido as apellido_docente
FROM cursos c
JOIN docentes d ON c.id_docente = d.id_docente;

SELECT c.nombre_curso, COUNT(i.id_inscripcion) AS numero_estudiantes
FROM cursos c
LEFT JOIN inscripciones i ON c.id_curso = i.id_curso
GROUP BY c.nombre_curso
ORDER BY numero_estudiantes DESC