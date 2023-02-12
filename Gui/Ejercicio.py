from tkinter import * 
from tkinter import ttk

raiz = Tk()
raiz.geometry("480x300")
raiz.title("Ejercicio Final")

#Contenedor Identificación
frame_personales = Frame(raiz, width=250, height=250, pady=3) 
frame_personales.grid(row=0, column=0)
frame_personales.config(relief="sunken")
frame_personales.config(bd=1) 

#Contenedor Aficiones
frame_aficiones = Frame(raiz, width=250, height=80)
frame_aficiones.grid(row=1, column=0)

#Contenedor Botones
frame_botones = Frame(raiz, width=250, height=25, padx=3, pady=3)
frame_botones.grid(row=2, column=0)

#Contenedor Ocupaciones
frame_ocupaciones = Frame(raiz, width=230, height=250)
frame_ocupaciones.grid(row=0, column=1)

#Contenedor Estados
frame_estados = Frame(raiz, width=230, height=80, pady=3)
frame_estados.grid(row=1, column=1)


#WIDGETS DATOS PERSONALES
lblNombre = Label(frame_personales, text="Nombre")
lblApaterno = Label(frame_personales, text="A. Paterno")
lblAmaterno = Label(frame_personales, text="A. Materno")
lblCorreo = Label(frame_personales, text="Correo")
lblMovil = Label(frame_personales, text="Móvil")

txtNombre = Entry(frame_personales)
txtApaterno = Entry(frame_personales)
txtAmaterno = Entry(frame_personales)
txtCorreo = Entry(frame_personales)
txtMovil = Entry(frame_personales)

lblAficiones = Label(frame_aficiones, text="Aficiones:")
chkLeer = Checkbutton(frame_aficiones, text="Leer")
chkMusica = Checkbutton(frame_aficiones, text="Música")
chkVideojuegos = Checkbutton(frame_aficiones, text="Videojuegos")

btnAceptar = Button(frame_botones, text="Guardar")
botCancelar = Button(frame_botones, text="Cancelar")

ocupacion = StringVar()
rbtEstudiante = Radiobutton(frame_ocupaciones, text="Estudiante", variable=ocupacion, value="Estudiante")
rbtEmpleado = Radiobutton(frame_ocupaciones, text="Empleado", variable=ocupacion, value="Empleado")
rbtDesempleado = Radiobutton(frame_ocupaciones, text="Desempleado", variable=ocupacion, value="Desempleado")

estado = StringVar()
lblEstados = Label(frame_estados, text="Seleccione Estado")
cmbEstados = ttk.Combobox(frame_estados, textvariable=estado)
cmbEstados['values'] = ("Estados 32","Aguascalientes","Baja California","Baja California Sur","Campeche","Chiapas","Chihuahua",
"Coahuila de Zaragoza","Colima","Ciudad de México","Durango","Guanajuato","Guerrero",
"Hidalgo","Jalisco","Estado de Mexico","Michoacan de Ocampo","Morelos","Nayarit","Nuevo Leon",
"Oaxaca","Puebla","Queretaro de Arteaga","Quintana Roo","San Luis Potosi","Sinaloa","Sonora",
"Tabasco","Tamaulipas","Tlaxcala","Veracruz","Yucatan","Zacatecas")


#POSICIONAMIENTO DE WIDGETS
        #Datos de identificación
lblNombre.grid(column=0, row=0, pady=5)
lblApaterno.grid(column=0, row=1, pady=5)
lblAmaterno.grid(column=0, row=2, pady=5)
lblCorreo.grid(column=0, row=3, pady=5)
lblMovil.grid(column=0, row=4, pady=5)
txtNombre.grid(column=1, row=0, padx=5, pady=5)
txtApaterno.grid(column=1, row=1, padx=5, pady=5)
txtAmaterno.grid(column=1, row=2, padx=5, pady=5)
txtCorreo.grid(column=1, row=3, padx=5, pady=5)
txtMovil.grid(column=1, row=4, padx=5, pady=5)

        #Aficiones
lblAficiones.grid(column=1, row=0, padx=10, pady=5)
chkLeer.grid(column=1, row=1,padx=5, pady=5)
chkMusica.grid(column=2, row=1, padx=5, pady=5)
chkVideojuegos.grid(column=3, row=1, padx=5, pady=5)

        #Botones
btnAceptar.grid(column=0, row=0, padx=10, pady=5)
botCancelar.grid(column=1, row=0, padx=10, pady=5)

        #Ocupaciones
rbtEstudiante.grid(column=0, row=0, sticky=W)
rbtEmpleado.grid(column=0, row=1, sticky=W)
rbtDesempleado.grid(column=0, row=2, sticky=W)

        #Estados
lblEstados.grid(column=0, row=0, padx=10, pady=5)
cmbEstados.grid(column=0, row=2, padx=5, pady=5)

raiz.mainloop()