#Escribe una función que pueda decirte si un año (número entero) es bisiesto o no.

def bisiesto(año:int):
    if (año % 4 == 0 and año % 100 != 0) or año % 400 == 0:
        print("Es año bisiesto")
    else:
        print("No es año bisiesto")

bisiesto(2004)