# Mi Blog — Blog Full-Stack con Panel de Administración

Blog personal construido desde cero con Flask, SQL Server, HTML/CSS/JavaScript y una API REST propia. Incluye un panel de administración protegido con autenticación, donde se pueden crear, editar y eliminar publicaciones en tiempo real, sin recargar la página.

Proyecto de aprendizaje full-stack, enfocado en entender cómo se conectan el frontend, el backend y la base de datos en una aplicación web real.

## Funcionalidades

- Blog público con posts renderizados dinámicamente desde SQL Server (Jinja2)
- API REST propia (`/api/posts`) con los 4 verbos HTTP: GET, POST, PUT, DELETE
- Panel de administración protegido con login (usuario/contraseña con hash seguro)
- Crear, editar y eliminar posts desde el panel, sin recargar la página (JavaScript + fetch)
- Sesiones de usuario con Flask-Login
- Rutas protegidas: solo el administrador autenticado puede modificar contenido

## Tecnologías

- **Python / Flask** — servidor web y lógica del backend
- **SQL Server** — base de datos relacional (tablas `Posts` y `Usuarios`)
- **pyodbc** — conexión entre Flask y SQL Server
- **Flask-Login** — manejo de sesiones y rutas protegidas
- **Werkzeug** — hashing seguro de contraseñas
- **Jinja2** — motor de plantillas para HTML dinámico
- **HTML / CSS** — estructura semántica y estilos
- **JavaScript (fetch, async/await, DOM)** — interactividad sin recargar la página
- **Git / GitHub** — control de versiones

## Arquitectura

El proyecto combina dos formas de generar contenido dinámico:
1. **Server-side con Jinja2**: el blog público (`/`) se genera en el servidor con los posts ya incluidos en el HTML.
2. **Client-side con JavaScript**: el panel de administración (`/admin`) consume la API propia con `fetch` para crear, editar y eliminar posts sin recargar la página.

## Cómo ejecutarlo

1. Clonar el repositorio
2. Crear un entorno virtual: `python -m venv venv`
3. Activarlo: `.\venv\Scripts\Activate.ps1`
4. Instalar dependencias: `pip install -r requirements.txt`
5. Crear la base de datos en SQL Server (ver sección "Base de datos")
6. Crear el usuario administrador ejecutando `python crear_admin.py`
7. Ejecutar: `python app.py`
8. Visitar `http://localhost:5000`

## Base de datos

```sql
CREATE DATABASE MiBlog;
GO
USE MiBlog;
GO

CREATE TABLE Posts (
    id INT IDENTITY(1,1) PRIMARY KEY,
    titulo NVARCHAR(200) NOT NULL,
    contenido NVARCHAR(MAX) NOT NULL,
    fecha_publicacion DATETIME NOT NULL DEFAULT GETDATE()
);

CREATE TABLE Usuarios (
    id INT IDENTITY(1,1) PRIMARY KEY,
    usuario NVARCHAR(50) NOT NULL UNIQUE,
    password_hash NVARCHAR(255) NOT NULL
);
```

## Endpoints de la API

| Método | Ruta                  | Descripción                  | Protegido |
|--------|-----------------------|-------------------------------|-----------|
| GET    | `/api/posts`           | Lista todos los posts         | No        |
| POST   | `/api/posts`           | Crea un post nuevo            | Sí        |
| PUT    | `/api/posts/<id>`      | Actualiza un post existente   | Sí        |
| DELETE | `/api/posts/<id>`      | Elimina un post               | Sí        |

## Estructura del proyecto






## Posibles mejoras futuras

- Subida de imágenes en los posts
- Editor de texto enriquecido (negritas, listas, etc.)
- Paginación de posts
- Búsqueda de posts
- Comentarios de visitantes

## Autor

Wilberth


















