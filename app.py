from flask import Flask, render_template
from database import listar_posts

app = Flask(__name__)

@app.route("/")
def inicio():
    posts = listar_posts()
    return render_template("index.html", posts=posts)

if __name__ == "__main__":
    app.run(debug=True)