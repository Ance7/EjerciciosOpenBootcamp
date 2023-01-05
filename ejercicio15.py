# En este segundo ejercicio, tendréis que crear una interfaz sencilla la cual debe de contener una lista de elementos seleccionables, 
# también debe de tener un label con el texto que queráis.

import tkinter
from tkinter import *

window = tkinter.Tk()
objeto = StringVar()
lista = ["Caja", "Pelota", "Cubo", "Cono"]

listbox = Listbox(window)
for i in lista:
 listbox.insert(END, i)
listbox.pack()

label = Label(text="Objetos en la lista")
label.pack()

window.mainloop()