#En este ejercicio tendréis que crear un módulo que contenga las operaciones básicas de una calculadora: sumar, restar, multiplicar y dividir.

#Este módulo lo importaréis a un archivo python y llamaréis a las funciones creadas. Los resultados tenéis que mostrarlos por consola.

import operaciones as op

def main():
    opsuma = op.suma(15, 53)
    print("Funcion suma: ", opsuma)


    opresta = op.restar(56, 34)
    print("Funcion restar: ", opresta)


    opmulti = op.multiplicar(5, 10)
    print("Funcion multiplicar: ", opmulti)


    opdiv = op.dividir(49, 7)
    print("Funcion suma: ", opdiv)

if __name__ == '__main__':
    main()