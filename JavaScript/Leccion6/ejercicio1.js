const ListaCompra = ['Huevos', 'Leche', 'Pan', 'Mantequilla', 'Cereal']
ListaCompra.push('Aceite de GIrasol')
ListaCompra.pop()

const Peliculas = [
    {titulo: 'Fractura', director: 'Brad Anderson', fecha: new Date (2019, 9, 22)},
    {titulo: 'Pinocho', director:'Gillermo del Toro', fecha: new Date (2022, 11, 24)},
    {titulo: 'El praticante', director: 'Carles Torras', fecha: new Date (2020, 9, 16)}
]
const Peliculas2010 = Peliculas.filter(obj => obj.fecha > new Date(2010, 1 ,1))
const Directores = Peliculas.map(obj => obj.director)
const Titulos = Peliculas.map(obj => obj.titulo)
const TituyDirec = Directores.concat(Titulos)
const TituyDirec2 = [...Directores, ...Titulos]