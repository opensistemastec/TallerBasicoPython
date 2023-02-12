from tkinter import *
from tkinter import ttk

class Conversor:
    def __init__(self, raiz): #Siempre el primer parametro es self.
        raiz.title("Pies a metros")

        mainFrame = ttk.Frame(raiz) #Devuelve un objeto tipo frame. Todos los marcos reciben como parametro la raiz
        mainFrame.grid(column=0, row=0)

        pies_entry = ttk.Entry(mainFrame)
        pies_entry.grid(column=2, row=0)

        ttk.Label(mainFrame, text="Soy una etiqueta").grid(column=2, row=2)
        ttk.Button(mainFrame, text="Calcular").grid(column=3, row=3)
        ttk.Label(mainFrame, text="Es equivalente a: ").grid(column=1, row=2)
        ttk.Label(mainFrame, text="metros").grid(column=3, row=2, sticky=W)

        pies_entry.focus()
        raiz.bind("<Return>", self.calcular)

def Calcular(self, *args):
    try:
        valor = float(self.pies.get())
        self.metros.set(int(0.3048 * valor * 10000.0 + 0.5)/10000.0)
    except ValueError:
        pass


raiz = Tk()#La raiz siempre debe ser objeto tipo TK.
Conversor(raiz)
raiz.mainloop() #Crea la ventana.

