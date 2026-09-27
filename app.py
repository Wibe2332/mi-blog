from flask import Flask, render_template, jsonify, request, redirect, url_for
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import check_password_hash
from database import listar_posts, conectar, crear_post, editar_post, eliminar_post

app = Flask(__name__)
app.secret_key = "cambia_esto_por_algo_secreto"

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


class Usuario(UserMixin):
    def __init__(self, id, usuario):
        self.id = id
        self.usuario = usuario


@login_manager.user_loader
def cargar_usuario(user_id):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT id, usuario FROM Usuarios WHERE id = ?", user_id)
    fila = cursor.fetchone()
    conexion.close()

    if fila:
        return Usuario(fila[0], fila[1])
    return None

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        usuario_form = request.form["usuario"]
        password_form = request.form["password"]

        conexion = conectar()
        cursor = conexion.cursor()
        cursor.execute("SELECT id, usuario, password_hash FROM Usuarios WHERE usuario = ?", usuario_form)
        fila = cursor.fetchone()
        conexion.close()

        if fila and check_password_hash(fila[2], password_form):
            usuario_obj = Usuario(fila[0], fila[1])
            login_user(usuario_obj)
            return redirect(url_for("admin"))
        else:
            return render_template("login.html", error="Usuario o contraseña incorrectos")

    return render_template("login.html")


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("inicio"))


@app.route("/admin")
@login_required
def admin():
    return render_template("admin.html")


@app.route("/")
def inicio():
    posts = listar_posts()
    return render_template("index.html", posts=posts)


@app.route("/api/posts")
def api_posts():
    posts = listar_posts()

    lista_posts = []
    for post in posts:
        lista_posts.append({
            "id": post[0],
            "titulo": post[1],
            "contenido": post[2],
            "fecha": str(post[3])
        })

    return jsonify(lista_posts)


@app.route("/api/posts", methods=["POST"])
@login_required
def api_crear_post():
    datos = request.get_json()
    crear_post(datos["titulo"], datos["contenido"])
    return jsonify({"mensaje": "Post creado"}), 201


@app.route("/api/posts/<int:id_post>", methods=["PUT"])
@login_required
def api_editar_post(id_post):
    datos = request.get_json()
    editar_post(id_post, datos["titulo"], datos["contenido"])
    return jsonify({"mensaje": "Post actualizado"})


@app.route("/api/posts/<int:id_post>", methods=["DELETE"])
@login_required
def api_eliminar_post(id_post):
    eliminar_post(id_post)
    return jsonify({"mensaje": "Post eliminado"})    

if __name__ == "__main__":
    app.run(debug=True)