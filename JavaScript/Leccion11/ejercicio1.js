class Estudiante {
    nombre = 'Anghelo'
    asignaturas = ['Javascript', 'HTML', 'CSS']

    obtendatos(){
        return {
            nombre: this.nombre,
            asignaturas: this.asignaturas
        }
    }
}

const estudiante = new Estudiante()
console.log(estudiante.obtendatos)