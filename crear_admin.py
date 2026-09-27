from werkzeug.security import generate_password_hash
from database import conectar

usuario = "wilberth"
password = "tu_contraseña_aqui"

password_hash = generate_password_hash(password)

conexion = conectar()
cursor = conexion.cursor()
cursor.execute(
    "INSERT INTO Usuarios (usuario, password_hash) VALUES (?, ?)",
    usuario, password_hash
)
conexion.commit()
conexion.close()

print("✅ Usuario admin creado")