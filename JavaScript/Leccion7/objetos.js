// Crea un archivo llamado objetos.js que contenga las siguientes líneas
// - Un objeto con tus datos personales (nombre, apellido, edad, altura, eresDesarrollador)
// - Una variable que obtenga tu edad a partir del objeto anterior
// - Una lista que contenga el objeto con tus datos personales y un nuevo objeto con los datos personales de tus dos mejores amig@s
// - Una nueva lista con los objetos de la lista anterior ordenados por edad, de mayor a menor

const datos = {
    nombre: "Anghelo",
    apellido: "Alva",
    edad: 19,
    altura: 1.70,
    eresDesarrollador: false
}

const edad1 = datos.edad
console.log(edad1)

const datos2 = {...datos}

datosamigos = [{...datos}, {
    nombre: "Sergio",
    apellido: "Arenas",
    edad: 19,
    altura: 1.77,
    eresDesarrollador: false
}, {
    nombre: "Mathiu",
    apellido: "Gomez",
    edad: 19,
    altura: 1.67,
    isDesarrollador: false
}]

const listaordenada = datosamigos.sort((a,b) => b.edad - a.edad)

console.log(listaordenada)