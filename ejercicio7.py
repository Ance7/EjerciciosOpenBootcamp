#En este segundo ejercicio, tendréis que crear un programa que tenga una clase llamada Alumno que tenga como atributos su nombre y su nota. 
#Deberéis de definir los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no.

class alumno():
    def atributos(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
    
    def imprimir(self):
        print("Nombre : ", self.nombre)
        print("Nota : ", self.nota)

    def resultado(self):
        if self.nota > 5:
            print("Haz aprovado")
        else:
            print("No haz aprovado")

alumno1 = alumno()
alumno1.atributos("Victor", 7)
alumno1.imprimir()
alumno1.resultado()
