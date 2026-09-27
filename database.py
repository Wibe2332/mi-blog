import pyodbc

def conectar():
    conexion = pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=Happy;"
        "DATABASE=MiBlog;"
        "Trusted_Connection=yes;"
    )
    return conexion


def listar_posts():
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT id, titulo, contenido, fecha_publicacion
        FROM Posts
        ORDER BY fecha_publicacion DESC
    """)

    filas = cursor.fetchall()
    conexion.close()
    return filas


def crear_post(titulo, contenido):
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute(
        "INSERT INTO Posts (titulo, contenido) VALUES (?, ?)",
        titulo, contenido
    )

    conexion.commit()
    conexion.close()


def editar_post(id_post, titulo, contenido):
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute(
        "UPDATE Posts SET titulo = ?, contenido = ? WHERE id = ?",
        titulo, contenido, id_post
    )

    conexion.commit()
    conexion.close()


def eliminar_post(id_post):
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("DELETE FROM Posts WHERE id = ?", id_post)

    conexion.commit()
    conexion.close()