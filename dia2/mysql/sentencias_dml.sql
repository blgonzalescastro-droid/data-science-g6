-- SENTENCIAS DML
-- CRUD
-- C - INSERT
-- R - SELECT
-- U - UPDATE
-- D - DELETE

--INSERT
insert into
    alumno (nro_documento, nombre)
values ('100', 'beatriz gonzales');
-- INSERTAR VARIOS REGISTROS
insert into
    alumno (nro_documento, nombre)
VALUES ('200', 'Ana Martinez'),
    ('300', 'Luis Lopes'),
    ('400', 'Jose Ponce'),
    ('500', 'Rodrigo Ibañez'),
    ('600', 'Martina Diaz'),
    ('700', 'Sara Perez'),
    ('800', 'Raul Rivera'),
    ('900', 'Sofia Castro'),
    ('1000', 'Jesus Ortiz');

update alumno SET email = 'codigo@gmail.com';
-- UPDATE CON WHERE
update alumno set email = 'beatriz@gmail.com' where id = 1;

--UPDATE CON FUNCIONES
update alumno
set
    email = CONCAT(
        lower(
            replace (nombre, ' ', '.')
        ),
        '@gmail.com'
    )
where
    id > 1;
--SELECT
SELECT * FROM alumno;

SELECT nombre, email from alumno;

SELECT nombre from alumno where id > 5;

select * from alumno order by nombre ASC;

--DELETE
delete from alumno where id = 10;