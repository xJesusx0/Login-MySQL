function mostrarModal(element) {
    document.getElementById("myModal").style.display = "block";
    window.url = element.getAttribute("modal-url")
    console.log(window.url)
}

function cerrarModal() {
    document.getElementById("myModal").style.display = "none";
}

function confirmarEliminacion() {
    window.location.href = url;
}

window.onclick = function(event) {
    var modal = document.getElementById("myModal");
    if (event.target == modal) {
        modal.style.display = "none";
    }
}
