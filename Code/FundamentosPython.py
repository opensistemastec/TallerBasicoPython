#Crear función
def nuevoTema(tema):
    print("=====", tema, "=====")

if __name__=="__main__":
    nuevoTema("Operadores aritméticos") #Invocar una función
    print("Operador exponente -> 5 ** 3 = ", 5 ** 3)
    print("Operador cociente -> 5 // 3 = ", 5 // 3)

    nuevoTema("Operadores lógicos")
    print("Operador<and> (True and False): ", True and False)

    #Actividad: Imprimir las tablas de verdad de los operadores lógicos (pendiente).

    ''' Este es un comentario
        en varias líneas '''

    nuevoTema("Operadores de comparación")
    print("2 == 3 -> ", 2 == 3)

    #Actividad: Agregar ejemplos de los operadores de comparación.
    

    nuevoTema("Variables")
    variable1 = 10
    _variable2 = 6.2832
    Variable3 = "juancho"
    dosPalabras = "Hola mundo"
    dos_palabras = "Estilo Python"

    print(variable1,"\n", _variable2, Variable3, dos_palabras, dos_palabras)

    #Asignación de variables en una sola línea
    nuevoTema("Asignación de variables en una sola línea")
    a, b, c = 5, 10.8, "Welcome"
    print(a)
    print(b)
    print(c)

    #Número enteros
    nuevoTema("Enteros")
    w = 105
    x = 45600040303
    y = -567
    z = 0b000110001 #dato binario
    h = 0xff #dato hexadecimal

    print(w, type(w))
    print(x, type(x))
    print(y, type(y))
    print(z, type(z))
    print(w, type(h))

    #Números flotantes
    nuevoTema("Flotantes")
    x = 1297.50
    print(x, type(x))
    y = 0.59594
    print(y, type(y))

   #Números complejos
    nuevoTema("Complejos")
    x = -46j
    y = 12 + 45j
    z = 2j
    print(x, type(x))
    print(y, type(y))
    print(z, type(z))

    #Booleanos
    nuevoTema("Booleanos")
    lis = [8]

    print(lis, "lis", bool(lis))
    val = None
    print(val, type(val))
    val = True
    print(val,  type(val))

    #Listas
    nuevoTema("Listas")
    a = [10, 20.5, "Python list", -45j]
    print(a, type(a))
    print(a[1], type(a))
    a[1]= "Hola"
    print(a[1], type(a))

    #Tuplas
    nuevoTema("Tuplas")
    t = (25, "tupla", 1 + 10j, 45.6)
    print(t)
    print(t[1])
    #t[1] = 20.3 Las tuplas son inmutables y se colocan entre ()
    #print(t)

    print("t[0:3] = ", t[0:3])

    #Diccionarios
    nuevoTema("Diccionarios")
    d = {1:"Valor1", 2:"Valor2", "Nombre":"Juanco"}
    print(d,type(d))
    print("d[1] = ", d[1])
    print("d[nombre] = ", d["Nombre"])

    #Cadenas
    nuevoTema("Cadenas")
    cadena1 = "Esto es una cadena"
    cadena2 = "Esto también es una cadena"

    print(cadena1, type(cadena1))
    print(cadena2, type(cadena2))

    cadenaMultilinea = ''' Esto es una cadena
    de varias líneas  con tabulares y 
    saltos
    de
    línea. '''

    print(cadenaMultilinea, type(cadenaMultilinea))
    
    cadena3 = ''
    print(cadena3, type(cadena3))

    print("Segmentación de cadenas:")
    print(cadena1[5:11])
    print(cadena1[:3])
    print(cadena1[7:])
    print(cadena1[-8:-1])
    print(cadena1[0:18:1])
    print(cadena1[0:18:2])
    print(cadena1[0:18:3])

    cadena4 = (cadena1 + " ") * 5
    print(cadena4)

    nuevoTema("Tipos mutables e inmutables")
    #Cada objeto está identificado por su identidad, tipo y valor.
    x = 10
    print("Identidad: ", id(x))
    print("Tipo: ", type(x))
    print("Valor: ", x)

    lista1 = [1, 2, 3, 4] #Declara una lista
    lista2 = list("6789")
    print(lista1)
    print(lista2)
    lista3 = [1, "Hola", 3.14, [1, 2, 3]]
    print(lista3)

    lista1 = [1, 2, 3, 4] #Declara una lista
    lista2 = ("6789")
    print(lista1)
    print(lista2)

    lista3 = [1,"Hola", 3.14, [1, 2, 3]]
    print(lista3)
    print(lista3[3][1])

    conjuntos = set(["Manzana", "Manzana", "Manzana", "Pera", "Durazno", "Durazno"]) #Muestra valores únicos
    print("Conjunto: ", conjuntos)

    diccionario = {
        "Nombre" : "Konrado",
        "Edad" : "38",
        456 : 123456789
    }

    print("Diccionario: ", diccionario)
    print("Diccionario nombre: ", diccionario[456])

    nuevoTema("Entrada de datos desde el teclado.")

    print("¿Cómo te llamas?")
    nombre = input()
    print("Hola", nombre)

    aPaterno = input("Cuál es tu apellido paterno?: ")
    print(nombre + " " + aPaterno)

    print(type(nombre))

    n1 = float(input("Ingresa un número: "))
    print(type(n1))

    n2 = float(input("Ingresa un número: "))
    print(type(n2))

    cientifico = (23E47)
    print(cientifico)

    print(n1 + n2)


































    