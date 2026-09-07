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