#En este ejercicio vais a crear la clase Vehículo la cual tendrá los siguientes atributos:
    #Color
    #Ruedas
    #Puertas
#Por otro lado crearéis la clase Coche la cual heredará de Vehículo y tendrá los siguientes atributos:
   #Velocidad
    #Cilindrada
#Por último, tendrás que crear un objeto de la clase Coche y mostrarlo por consola.

class ejercicio():
    color="Negro"
    ruedas=4
    puertas=4

class coche(ejercicio):
    velocidad="180Km/h"
    cilindrada="nose"

coche1=coche()
print("Color: ",coche1.color)
print("Cantidad de ruedas: ", coche1.ruedas)
print("Cantidad de puertas: ",coche1.puertas)
print("Velocidad : ",coche1.velocidad)
print("Cilindrada: ",coche1.cilindrada)