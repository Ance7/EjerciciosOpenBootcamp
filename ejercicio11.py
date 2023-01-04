# En este segundo ejercicio, tendréis que crear un archivo py y dentro crearéis una clase Vehículo, 
# haréis un objeto de ella, lo guardaréis en un archivo y luego lo cargamos.

import pickle

class Vehiculo:
    def __init__(self, puertas, ruedas, color):
        self.puertas = puertas
        self.ruedas = ruedas
        self.color = color

Vehiculo1 = Vehiculo(4, 4, "rojo")

f = open('archivo2.txt', 'wb')
pickle.dump(Vehiculo1, f)
f.close()

f = open('archivo2.txt', 'r')
Objeto = pickle.load(f)
f.close()

print(type(Objeto)) 