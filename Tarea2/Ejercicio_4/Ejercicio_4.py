class Bus:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.pasajeros = 0
        self.pasaje = 1.50

    def pasajeros_abordo(self, cantidad):
        if self.pasajeros + cantidad <= self.capacidad:
            self.pasajeros += cantidad
            return f"{cantidad} pasajeros abordaron el bus. Total de pasajeros: {self.pasajeros}"
        return "No se pueden abordar más pasajeros"

    def pasaje_cobrar(self):
        total = self.pasaje * self.pasajeros
        print(f"El total del pasaje es: {total} Bs")

    def asientos_disponibles(self):
        disponibles = self.capacidad - self.pasajeros
        print(f"Asientos disponibles: {disponibles}")

    def __str__(self):
        return f"Bus(capacidad={self.capacidad}, pasajeros={self.pasajeros}, pasaje={self.pasaje})"

class Main():
    bus = Bus(capacidad=50)
    print(bus.pasajeros_abordo(10))
    print(bus.pasajeros_abordo(15))
    bus.pasaje_cobrar()
    bus.asientos_disponibles()
    print(bus)

