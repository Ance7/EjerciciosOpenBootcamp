# En este segundo ejercicio, tenéis que crear una aplicación que obtendrá los elementos impares de una lista pasada por parámetro con 
# filter y realizará una suma de todos estos elementos obtenidos mediante reduce. 

from functools import reduce

def operacion(lista): 
    resultado = list(filter((lambda x: x % 2), lista)) 
    resultado = reduce( (lambda x, y: x + y), resultado) 
    print(resultado)

lista = (51, 23, 56, 34, 93, 29)

operacion(lista)