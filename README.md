## Ejecución del proyecto con Docker

Este proyecto utiliza Docker para ejecutar una aplicación Python que se conecta a una base de datos PostgreSQL, inserta personajes y permite consultar los datos almacenados.

### 1. Configurar las variables de entorno

Crear un archivo `.env` en la raíz del proyecto con las siguientes variables:

```env
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=postgres

DATABASE_URL=postgresql://postgres:postgres@db-reto:5432/postgres
```

### 2. Arrancar la base de datos

Desde la raíz del proyecto, ejecutar:

```bash
docker compose up -d db-reto
```

Este comando inicia PostgreSQL en segundo plano utilizando la configuración definida en `compose.yaml`.

La base de datos estará disponible en el puerto `5434` del equipo anfitrión y en el puerto `5432` dentro de la red Docker.

### 3. Construir la imagen de Python

Construir la imagen a partir del `Dockerfile`:

```bash
docker compose build app
```

Este proceso instala Python 3.12 y las dependencias indicadas en `requirements.txt`.

### 4. Ejecutar la aplicación

Ejecutar la aplicación Python desde su contenedor:

```bash
docker compose run --rm app
```

Docker Compose conecta automáticamente el contenedor Python con PostgreSQL mediante la red interna, utilizando el nombre del servicio `db-reto`.

La aplicación ejecuta el archivo `main.py`, que permite realizar la carga y consulta de los personajes.

Para insertar los personajes, debe estar habilitado el código de inserción en `main.py`. Para comprobar los datos guardados, se puede ejecutar la parte de consultas.

### 5. Comprobar los resultados

La aplicación muestra en consola los primeros diez personajes ordenados por identificador, indicando su ID, nombre y especie.

También muestra el número total de personajes almacenados en la base de datos.

### 6. Detener los contenedores

Para detener PostgreSQL y eliminar los contenedores y la red creados por Docker Compose:

```bash
docker compose down
```

Los datos almacenados se conservan gracias al volumen `postgres_data`.

## 👥 Integrantes del equipo y reparto de tareas

El proyecto ha sido desarrollado en equipo, distribuyendo las responsabilidades de acuerdo con los requisitos del reto.

| Integrante | Responsabilidades |
|---|---|
| **Christian** | Creación y configuración del repositorio de GitHub, gestión de colaboradores, preparación del entorno Docker, configuración de PostgreSQL en `compose.yaml` y creación del volumen persistente. |
| **Jade** | Configuración de las variables de entorno (`.env.example`), conexión entre Python y PostgreSQL mediante `psycopg` y creación de la tabla `characters` con sus campos y restricciones. |
| **Pablo** | Preparación de los datos de los personajes, desarrollo de las sentencias `INSERT` e inserción de registros mediante `cur.executemany()`. |
| **Antonio** | Implementación de las consultas `SELECT`, recuperación de registros mediante `fetchall()`, recuento total de personajes con `COUNT(*)`, pruebas de funcionamiento y documentación de ejecución en el `README.md`. |

### 🤝 Colaboración y organización

- Todos los integrantes participan en la revisión y comprobación del funcionamiento del proyecto.
- Se utiliza GitHub para gestionar el código fuente y colaborar mediante ramas y *Pull Requests*.
- Se realiza al menos una *Pull Request* para integrar y revisar los cambios.
- Se comprueba conjuntamente que los personajes se almacenan correctamente en PostgreSQL y que las consultas muestran los resultados esperados.
- Se verifica que la aplicación puede ejecutarse desde el contenedor Python mediante Docker Compose.