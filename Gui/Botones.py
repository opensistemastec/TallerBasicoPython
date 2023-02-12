from tkinter import *
from tkinter import ttk

raiz = Tk()
raiz.title("Botones")
boton = ttk.Button(raiz, text="Botón sólo texto")
boton.grid(column=0, row=1)

imagen = PhotoImage(file="Link.png")

btnImagen = ttk.Button(raiz)
btnImagen.grid()
btnImagen['image'] = imagen

btnCombinada = ttk.Button(raiz, text="btnCombinada", compound="bottom")
btnCombinada.grid()
btnCombinada['image'] = imagen

chkBoton = ttk.Checkbutton(raiz, text="Opción 1")
chkBoton.grid()

raiz.mainloop()