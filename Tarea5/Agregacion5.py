class Animal:
    def __init__(self, nombre, edad, nombreDueno):
        self.nombre = nombre
        self.edad = edad
        self.nombreDueno = nombreDueno

    def mostrar(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}, Dueño: {self.nombreDueno}")

class Perro(Animal):
    def __init__(self, nombre, edad, nombreDueno, requiereBosal, ladraFuerte):
        super().__init__(nombre, edad, nombreDueno)
        self.requiereBosal = requiereBosal
        self.ladraFuerte = ladraFuerte

    def mostrar(self):
        super().mostrar()
        print(f"Requiere bosal: {self.requiereBosal}, Ladra fuerte: {self.ladraFuerte}")

class Gato(Animal):
    def __init__(self, nombre, edad, nombreDueno, cazaRatones, tomaLeche):
        super().__init__(nombre, edad, nombreDueno)
        self.cazaRatones = cazaRatones
        self.tomaLeche = tomaLeche

    def mostrar(self):
        super().mostrar()
        print(f"Caza ratones: {self.cazaRatones}, Toma leche: {self.tomaLeche}")

class CentroVeterinario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.perros = []
        self.gatos = []

    def agregarPerro(self, perro):
        if len(self.perros) < 100:
            self.perros.append(perro)

    def agregarGato(self, gato):
        if len(self.gatos) < 100:
            self.gatos.append(gato)

    def mostrarTodo(self):
        print(f"\nCentro: {self.nombre}")
        print("Perros:")
        for p in self.perros:
            p.mostrar()
        print("Gatos:")
        for g in self.gatos:
            g.mostrar()

    def ordenarPerros(self):
        self.perros.sort(key=lambda p: (p.edad, p.nombreDueno, p.nombre))

    def ordenarGatos(self):
        self.gatos.sort(key=lambda g: (not g.tomaLeche, -g.edad, g.nombre))

    def contarAnimalesPorDueno(self):
        conteo = {}

        for p in self.perros:
            conteo[p.nombreDueno] = conteo.get(p.nombreDueno, 0) + 1

        for g in self.gatos:
            conteo[g.nombreDueno] = conteo.get(g.nombreDueno, 0) + 1

        for dueno, cantidad in conteo.items():
            if cantidad > 1:
                print(f"{dueno} tiene {cantidad} animales")

class Main:
    c1 = CentroVeterinario("Centro Norte")
    c2 = CentroVeterinario("Centro Sur")

    p1 = Perro("Max", 5, "Juan", True, True)
    p2 = Perro("Rocky", 3, "Ana", False, True)
    p3 = Perro("Luna", 5, "Juan", True, False)
    p4 = Perro("Toby", 2, "Luis", False, False)

    g1 = Gato("Michi", 4, "Ana", True, True)
    g2 = Gato("Pelusa", 2, "Carlos", False, True)
    g3 = Gato("Garfield", 6, "Juan", False, False)
    g4 = Gato("Nina", 3, "Luis", True, True)

    c1.agregarPerro(p1)
    c1.agregarPerro(p2)
    c1.agregarGato(g1)
    c1.agregarGato(g2)

    c2.agregarPerro(p3)
    c2.agregarPerro(p4)
    c2.agregarGato(g3)
    c2.agregarGato(g4)

    c1.mostrarTodo()
    c2.mostrarTodo()

    print("\nPerros ordenados:")
    c1.ordenarPerros()
    c1.mostrarTodo()

    print("\nGatos ordenados:")
    c1.ordenarGatos()
    c1.mostrarTodo()

    print("\nDueños con varios animales en Centro 1:")
    c1.contarAnimalesPorDueno()

    print("\nDueños con varios animales en Centro 2:")
    c2.contarAnimalesPorDueno()