# En este ejercicio, tendréis que crear un archivo py donde creéis un archivo txt, lo abráis y escribáis dentro del archivo. 
# Para ello, tendréis que acceder dos veces al archivo creado.

f = open ('archivo.txt', 'w')
f.write ("linea 1 \n")
f.close ()

f = open ('archivo.txt', 'r+')
f.readline()
f.write ("linea 2")
f.close ()
