#En este ejercicio tenéis que crear una lista de RadioButton que muestre la opción que se ha seleccionado y que contenga un 
# botón de reinicio para que deje todo como al principio.

#Al principio no tiene que haber una opción seleccionada

import tkinter
from tkinter import *

def seleccionado():
    print("Opcion seleccionada: ", opcion.get())
def reset():
    opcion.set(None)
    ventana.config(text="")

window = tkinter.Tk()
opcion = StringVar()
opcion.set(None)

Radiobutton(window, text="Boton1", variable=opcion, value='1', command=seleccionado).pack(anchor=W)

Radiobutton(window, text="Boton2", variable=opcion, value='2', command=seleccionado).pack(anchor=W)

Radiobutton(window, text="Boton3", variable=opcion, value='3', command=seleccionado).pack(anchor=W)

ventana = Label(window)
ventana.pack()
Button(window, text="Reinicio", command=reset).pack()

window.mainloop()