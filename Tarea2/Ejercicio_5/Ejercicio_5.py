class Jugador:
    def __init__(self, nombre, diamantes):
        self.nombre = nombre
        self.diamantes = diamantes

    def stacks_diamantes(self):
        return self.diamantes // 64

    def __str__(self):
        return f"Jugador(nombre={self.nombre}, diamantes={self.diamantes})"


class ServidorMinecraft:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.jugadores = []  

    def agregar_jugador(self, jugador):
        if len(self.jugadores) < self.capacidad:
            self.jugadores.append(jugador)
            return f"Jugador {jugador.nombre} agregado al servidor."
        else:
            return "Servidor lleno el server xdd"
    def mostrar_stacks(self):
        info = []
        for j in self.jugadores:
            info.append(f"{j.nombre} tiene {j.stacks_diamantes()} stacks de diamantes")
        return "\n".join(info)
    
    def jugador_mas_diamantes(self):
        diamantes_vector = [j.diamantes for j in self.jugadores]
        max_diamantes = max(diamantes_vector)
        for j in self.jugadores:
            if j.diamantes == max_diamantes:
                return f"Jugador con más diamantes: {j.nombre} ({j.diamantes} diamantes)"

    def total_diamantes(self):
        total = sum([j.diamantes for j in self.jugadores])
        return f"Total de diamantes en el servidor: {total}"
    
class Main:
    servidor = ServidorMinecraft(capacidad=10)

    jugadores = [
        Jugador("Loading...", 175),
        Jugador("Awitadecoco", 45),
        Jugador("Ajolotexd", 300),
        Jugador("Tusapato", 64)
    ]

    for j in jugadores:
        print(servidor.agregar_jugador(j))
    nuevo_jugador = Jugador("XxElProtaxX", 150)
    print(servidor.agregar_jugador(nuevo_jugador))


    print(servidor.mostrar_stacks())

    print("\n" + servidor.jugador_mas_diamantes())

    print(servidor.total_diamantes())
