from multimethod import multimethod

class Videojuego:
    @multimethod
    def __init__(self):
        self.nombre = "Roblox"
        self.plataforma = "PS5"
        self.cantidadJugadores = 10

    @multimethod
    def __init__(self, nombre:str, plataforma:str, cantidadJugadores:int):
        self.nombre = nombre
        self.plataforma = plataforma
        self.cantidadJugadores = cantidadJugadores

    @multimethod
    def agregarJugador(self):
        self.cantidadJugadores += 1

    @multimethod
    def agregarJugador(self, cantidad:int):
        self.cantidadJugadores += cantidad

    def __str__(self):
        return f"Videojuego: {self.nombre}, plataforma: {self.plataforma}, cantidadJugadores: {self.cantidadJugadores}"
    
class Main:
    v1 = Videojuego()
    v1.agregarJugador()
    print(v1)
    v2 = Videojuego("Fortnite", "Consola", 100)
    v2.agregarJugador(50)
    print(v2)
