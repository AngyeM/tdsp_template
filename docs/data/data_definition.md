# Definición de los datos

## Origen de los datos

El formato inicial del corpus son archivos de PDF basados en texto, que contienen información relacionada de pacientes oncológicos

## Especificación de los scripts para la carga de datos

Utilizando python se extrae el texto plano de los archivos y se consolida en una tabla en una base de datos basada en Postgres

## Referencias a rutas o bases de datos origen y destino

La base de datos con la que se trabaja es Redshift, la conexión se realiza utilizando directamente el host, usuario y contraseña.

### Rutas de origen de datos

Los archivos iniciales se almacenan de forma local, en un directorio se encuentran directamente los ficheros sin estructuras de subcarpetas.

### Base de datos de destino

El siguiente proceso se realiza para cada soporte:

- Extraer el texto
- Obtener metadatos del fichero (nombre, número de páginas)
- Los soportes cuentan con una nomeclatura que permite identificar la fecha de creación del fichero y la especialidad por lo tanto se extraen estos datos
