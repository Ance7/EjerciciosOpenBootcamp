let nombre = 'Anghelo'
let apellido = "Alva"
let estudiante = nombre.concat(` `).concat(apellido)

let estudianteMayus = estudiante.toUpperCase
let estudianteMinus = estudiante.toLocaleLowerCase
let cantidadCaracteres = estudiante.length
let primeraLetra = nombre.substring(0, 1)
let ultimaLetra = apellido.substring(apellido.length -1, apellido.length)
let sinEspacios = estudiante.replace(" ", "")
let Booleano = estudiante.includes(nombre)

