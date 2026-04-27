class Libro:
    def __init__(self, nombre, autor, anio):
        self.nombre = nombre
        self.autor = autor
        self.anio = anio

    def mostrar(self):
        print(f"Nombre: {self.nombre}, Autor: {self.autor}, Año: {self.anio}")

class Biblioteca:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros = []

    def agregarLibro(self, libro):
        if len(self.libros) < 100:
            self.libros.append(libro)

    def mostrarLibros(self):
        print(f"\nBiblioteca: {self.nombre}")
        for libro in self.libros:
            libro.mostrar()

    def buscarLibro(self, nombreBuscado):
        encontrado = False
        for libro in self.libros:
            if libro.nombre.lower() == nombreBuscado.lower():
                libro.mostrar()
                encontrado = True
        if not encontrado:
            print(f"Libro no encontrado en {self.nombre}")

class Main:
    b1 = Biblioteca("Principal")
    b2 = Biblioteca("Zona Norte")

    l1 = Libro("El Quijote", "Cervantes", 1605)
    l2 = Libro("Cien Años de Soledad", "García Márquez", 1967)
    l3 = Libro("1984", "George Orwell", 1949)
    l4 = Libro("El Principito", "Antoine de Saint-Exupéry", 1943)

    b1.agregarLibro(l1)
    b1.agregarLibro(l2)

    b2.agregarLibro(l3)
    b2.agregarLibro(l4)

    b1.mostrarLibros()
    b2.mostrarLibros()

    print("\nBuscando libro:")
    b1.buscarLibro("1984")

    print("\nBiblioteca con más libros:")
    if len(b1.libros) > len(b2.libros):
        print(b1.nombre)
    elif len(b2.libros) > len(b1.libros):
        print(b2.nombre)
    else:
        print("Empate:")
        print(b1.nombre)
        print(b2.nombre)