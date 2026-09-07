from flask import Flask, render_template, jsonify
from database import listar_posts

app = Flask(__name__)

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

if __name__ == "__main__":
    app.run(debug=True)