function mostrarModal() {
    document.getElementById("myModal").style.display = "block";
}

function cerrarModal() {
    document.getElementById("myModal").style.display = "none";
}

function confirmarEliminacion() {
    window.location.href = "/auth/delete-account";
}

window.onclick = function(event) {
    var modal = document.getElementById("myModal");
    if (event.target == modal) {
        modal.style.display = "none";
    }
}
