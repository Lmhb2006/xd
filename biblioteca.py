
def cargar_catalogo():
    biblioteca = {}
    with open("catalogo.txt", encoding="utf-8") as archivo:
        for linea in archivo:
            isbn, titulo, autor, genero, paginas = linea.strip().split(";")
            biblioteca[isbn] = {
                "titulo": titulo,
                "autor": autor,
                "genero": genero,
                "paginas": int(paginas)
            }
        return biblioteca


def cargar_almacen():
    historial = {}
    with open("almacen de libros.txt", "r+",encoding="utf-8") as archivo:
        for linea in archivo:
            nombre, isbn, autor, estado = linea.strip().split(";")
            historial[nombre] = {
                "isbn": isbn,
                "autor": autor,
                "estado": estado
            }
        return historial
    
def buscar_isbn(diccionario,isbn):
    if str(isbn) in diccionario.keys():
        ficha  = diccionario[isbn]
        print(ficha["titulo"],",", ficha["autor"],",", ficha["genero"],",", ficha["paginas"])
    else:
        print("ese libro no está")

def genero(diccionario,genero):
    lista_genero = []
    for k,v in diccionario.items():
        if v["genero"] == genero:
            libro = (v["titulo"], v["autor"])
            lista_genero.append(libro)
    for e in lista_genero:
        print(e)

## el codigo por auto con mas paginas es lo mismo pero toca sumar, ej: recorrer todo el catalog, sacar autor y ir sumando las pagias de cada libro
## deberia ser J. R.

def paginas_autor(diccionario, autor):
    total = 0
    for k,v in diccionario.items():
        if v["autor"] == autor:
            total += v["paginas"]
    print("El autor", autor, "tiene", total, "paginas en total")

Libros = cargar_catalogo()

historial = cargar_almacen()

"""buscar_isbn(diccionario, "9780060883287")

genero(diccionario, "Fantasía épica")

paginas_autor(diccionario, "Gabriel García Márquez")"""

def prestado(nombre, isbn):
    almacen = {}
    for libro in Libros:
        nombre = libro.strip().split(";")[0:2]
        almacen[nombre] = {
                "isbn": isbn
            }
        if isbn in almacen:
            prestado = True
            if prestado == False:
                    estado = "Prestado"
                    print("el libro se ha prestado correcramente")
                    historial[nombre].write(f"{isbn};{autor}")
            elif prestado == True:
                print("no se puede prestar, porque alguien más ya lo pidió :(")
        return almacen
    

"""for k,v in diccionario.items():
    print(k,"->",v)"""

"""prestado("Juan", "9788403512119")"""

def devolver(nombre, isbn):
    almacen = {}
    for libro in almacen:
        nombre, isbn = libro.strip().split(";") [0:2]
        almacen[nombre] = {
                "isbn": isbn,
                "autor": autor
            }
        if isbn in almacen.keys():
            prestado = True
            if prestado == True:
                    estado = "Devuelto"
                    print("el libro se ha devuelto correcramente")
                    historial[nombre].write(f"{nombre};{isbn};{autor}")
            elif prestado == False:
                print("ese libro no se ha prestado aun")
                break
        return almacen

def ver_prestados():
    historial = {}
    with open("almacen de libros.txt", encoding="utf-8") as file:
        for line in file:
            nombre, isbn = line.strip().split(";")
            historial[nombre] = {
                "isbn", isbn,
            }
        return historial

disponible = ver_prestados

opcion = 0

def menu():
    print("bienvenido a la biblioteca (•̀ᴗ•́)و ̑̑")
    print("aqui está el catalogo, a continuacion te mostrare un menu de opciones por si deseas algo:")
    print("bien, aqui estan las opciones:")
    print("1. buscar un libro por su isbn.")
    print("2. buscar un libro por su genero.")
    print("3. buscar cuantas paginas tiene un autor por sus obras.")
    print("4. pedir prestado un libro.")
    print("5. regresar un libro.")
    print("6. ver que libros estan prestados.")
    print("7. ver el catalogo de nuevo.")
    print("8. salir.")

menu()
while opcion != 8:

    opcion = int(input("ingrese la opcion que le interese o la que desea hacer:  "))

    if opcion == 1:
        isbn = str(input("ingrese el isbn del libro que busca: "))
        buscar_isbn(Libros, isbn)

    elif opcion == 2:
        genero = str(input("ingrese el genero del libro que busca: "))
        genero(Libros, genero)

    elif opcion == 3:
        autor = str(input("ingrese el nombre del autor que quiere investigar: "))
        paginas_autor(Libros, autor)

    elif opcion == 4:
        x = str(input("ingrese el ibsn del libro que desea: "))
        nombre = str(input("ingrese su nombre: "))
        prestado(nombre, x)
        print("el préstamo se hizo con éxito, おめでとう!(＾▽＾)")

    elif opcion == 5:
        isbn = str(input("ingrese el ibsn del libro que desea: "))
        nombre = str(input("ingrese su nombre: "))
        devolver(nombre, isbn)
        print("Gracias por devolver el libro, ありがとうございます!(⌒▽⌒)☆")

    elif opcion == 6:
        for k,v in disponible.items():
            print(k, "->", v)

    elif opcion == 7:
        for k,v in Libros.items():
            print(k,"->",v)
    
    elif opcion == 8:
        break

    else:
        print("por favor ingrese un numero entre las opciones que se le indicaron.")
        break

    break