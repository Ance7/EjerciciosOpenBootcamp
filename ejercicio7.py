#En este segundo ejercicio, tendréis que crear un programa que tenga una clase llamada Alumno que tenga como atributos su nombre y su nota. 
#Deberéis de definir los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no.

class alumno():
    def mostrarnota(nombre, nota):
        nombre = nombre
        nota = nota

        if nota > 5:
            print(nombre, "haz aprovado")
        else:
            print(nombre, "No haz aprovado")

alumno.mostrarnota("Victor", 7)