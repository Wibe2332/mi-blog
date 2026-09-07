const boton = document.getElementById("btn-actualizar");

boton.addEventListener("click", function () {
    fetch("/api/posts")
        .then(function (respuesta) {
            return respuesta.json();
        })
        .then(function (posts) {
            const contenedor = document.getElementById("contenedor-posts-js");
            contenedor.innerHTML = "";

            posts.forEach(function (post) {
                contenedor.innerHTML += `
                    <article>
                        <h2>${post.titulo}</h2>
                        <p>${post.contenido}</p>
                        <small>${post.fecha}</small>
                    </article>
                `;
            });
        });
});