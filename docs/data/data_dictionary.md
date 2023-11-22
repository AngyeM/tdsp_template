# Diccionario de datos

## Soportes Clinicos

**Estructura de Tabla 

| Variable | Descripción | Tipo de dato | Rango/Valores posibles | Fuente de datos |
| --- | --- | --- | --- | --- |
| tipo_archivo |Corresponde a la especialidad médica relacionada con el soporte | Texto | 255 | Nombre del archivo |
| fecha | Fecha del seguimiento del paciente relacionada al soporte | Fecha | YYYY-MM-DD | Nombre del archivo |
| metadatos | Metadatos relacionados al soporte | JSON | Diccionario clave-valor | Soporte |
| Contenido | Texto plano relacionado al soporte | Texto | 25000 | Soporte |
| chunk | Sección de la extracción | Numerico | Entero | proceso de extracción |

- **Variable**: nombre de la variable.
- **Descripción**: breve descripción de la variable.
- **Tipo de dato**: tipo de dato que contiene la variable.
- **Rango/Valores posibles**: rango o valores que puede tomar la variable.
- **Fuente de datos**: fuente de los datos de la variable.
