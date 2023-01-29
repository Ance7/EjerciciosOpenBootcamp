let nombre = "Anghelo"
let apellido = "Alva"
let nombreApellido = {
    nombre,
    apellido
}

// sessionStorage.setItem("nombreApellido", JSON.stringify(nombreApellido))

// localStorage.setItem("nombreApellido", JSON.stringify(nombreApellido))

const hora = new Date()

document.cookie = `nombreApellido=${JSON.stringify(nombreApellido)};expires=${new Date(now.getTime() + 2 * 60000).toUTCString}`