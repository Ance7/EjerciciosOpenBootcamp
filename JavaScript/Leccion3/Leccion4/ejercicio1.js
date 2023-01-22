let nombre = "Anghelo";
let apellido = "Alva";
let estudiante = nombre.concat(" ").concat(apellido);

let estudianteMayus = estudiante.toUpperCase();

let estudianteMinus = estudiante.toLowerCase();

let cantidadCaracteres = estudiante.length;

let PrimeraLetra = nombre.substring(0, 1);

let UltimaLetra = apellido.substring(apellido.length - 1);

let SinEspacios = estudiante.replace(" ", "");

let Booleano = estudiante.includes(nombre);
console.log(Booleano);