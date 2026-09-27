const inputId = document.getElementById("post-id");
const inputTitulo = document.getElementById("input-titulo");
const inputContenido = document.getElementById("input-contenido");
const btnGuardar = document.getElementById("btn-guardar");
const btnCancelar = document.getElementById("btn-cancelar");
const formTitulo = document.getElementById("form-titulo");
const listaPosts = document.getElementById("lista-posts");


async function cargarPosts() {
    const respuesta = await fetch("/api/posts");
    const posts = await respuesta.json();

    listaPosts.innerHTML = "";

    posts.forEach(function (post) {
        listaPosts.innerHTML += `
            <div class="post-admin">
                <h3>${post.titulo}</h3>
                <p>${post.contenido}</p>
                <button onclick="editarPost(${post.id}, '${post.titulo}', \`${post.contenido}\`)">Editar</button>
                <button onclick="borrarPost(${post.id})">Eliminar</button>
            </div>
        `;
    });
}


btnGuardar.addEventListener("click", async function () {
    const titulo = inputTitulo.value;
    const contenido = inputContenido.value;
    const id = inputId.value;

    if (id) {
        await fetch(`/api/posts/${id}`, {
            method: "PUT",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ titulo, contenido })
        });
    } else {
        await fetch("/api/posts", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ titulo, contenido })
        });
    }

    limpiarFormulario();
    cargarPosts();
});


function editarPost(id, titulo, contenido) {
    inputId.value = id;
    inputTitulo.value = titulo;
    inputContenido.value = contenido;
    formTitulo.textContent = "Editando post";
    btnCancelar.style.display = "inline-block";
}


btnCancelar.addEventListener("click", limpiarFormulario);


function limpiarFormulario() {
    inputId.value = "";
    inputTitulo.value = "";
    inputContenido.value = "";
    formTitulo.textContent = "Crear nuevo post";
    btnCancelar.style.display = "none";
}


async function borrarPost(id) {
    if (confirm("¿Seguro que quieres eliminar este post?")) {
        await fetch(`/api/posts/${id}`, { method: "DELETE" });
        cargarPosts();
    }
}


cargarPosts();