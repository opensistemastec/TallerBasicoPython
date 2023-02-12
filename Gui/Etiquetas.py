from tkinter import *
from tkinter import ttk
#from PIL import Image, ImageTk

raiz = Tk()
raiz.title("Etiquetas")
etqTexto = ttk.Label(raiz, text="Etiqueta sólo texto 1")
etqTexto.grid(column=0, row=1)

imagen = PhotoImage(file="Link.png")

#imagen = ImageTk.PhotoImage(Image.open('Link.png'))

etqImagen = ttk.Label(raiz)
etqImagen.grid()
etqImagen['image'] = imagen

etqCombinada = ttk.Label(raiz, text="etqCombinada", compound="bottom")
etqCombinada.grid()
etqCombinada['image'] = imagen


raiz.mainloop()