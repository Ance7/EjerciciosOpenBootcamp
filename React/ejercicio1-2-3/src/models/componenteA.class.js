export class Contacto {
    Nombre = ''
    Apellido = ''
    Email = ''
    Conectado = false

    constructor(nombre, apellido, email, conectado) {
        this.nombre = nombre
        this.apellido = apellido
        this.email = email
        this.conectado = conectado
    }
}