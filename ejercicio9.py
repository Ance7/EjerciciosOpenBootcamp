#En este segundo ejercicios tendréis que crear un script que nos diga si es la hora de ir a casa.
#Tendréis que hacer uso del modulo time. Necesitaréis la fecha del sistema y poder comprobar la hora.

#En el caso de que sean más de las 7, se mostrará un mensaje y en caso contrario, haréis una operación para calcular el tiempo que queda de trabajo.

import time

hora = time.strftime('%H')
minuto = time.strftime('%M')

if int(hora) >= 19:
    print("Ya es hora de irse")

else: 
    print("Aun no es hora de irse, quedan:", 18 - int(hora), "horas y ", 59 - int(minuto), "minutos")