document.addEventListener("DOMContentLoaded", function () {
    const preloader = document.getElementById("pageloader-overlay");

    // Simula la carga de la página (puedes ajustar el tiempo según necesites)
    setTimeout(() => {
        preloader.classList.add("hidden");
    }, 2000); // 2 segundos antes de ocultar el preloader
});
