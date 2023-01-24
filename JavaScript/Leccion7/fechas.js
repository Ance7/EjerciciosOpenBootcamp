const fecha = new Date()

const nacimiento = new Date(2003, 8, 19)

const tarde = fecha > nacimiento

const dianacimiento = nacimiento.getDate()
const mesnacimiento = nacimiento.getMonth() + 1
const anonacimiento = nacimiento.getFullYear()