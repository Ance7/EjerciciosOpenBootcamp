#En este ejercicio vais a crear la clase Vehículo la cual tendrá los siguientes atributos:
    #Color
    #Ruedas
    #Puertas
#Por otro lado crearéis la clase Coche la cual heredará de Vehículo y tendrá los siguientes atributos:
   #Velocidad
    #Cilindrada
#Por último, tendrás que crear un objeto de la clase Coche y mostrarlo por consola.

class ejercicio():
    def __init__(self, color, ruedas, puertas):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas

class coche(ejercicio):
    def __init__(self, color, ruedas, puertas, velocidad, cilindrada):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas
        self.velocidad = velocidad
        self.cilindrada = cilindrada

coche1=coche("Verde", 4, 4, "180km/h", 1000)
print("Color: ",coche1.color)
print("Cantidad de ruedas: ", coche1.ruedas)
print("Cantidad de puertas: ",coche1.puertas)
print("Velocidad : ",coche1.velocidad)
print("Cilindrada: ",coche1.cilindrada)
