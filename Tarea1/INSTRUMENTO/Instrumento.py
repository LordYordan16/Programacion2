class Instrumento:
    def __init__(self, nombre: str, material: str, tipo: str):
        self.nombre = nombre        
        self.__material = material  
        self.__tipo = tipo          

    def getMaterial(self):
        return self.__material

    def getTipo(self):
        return self.__tipo


    def setMaterial(self, material: str):
        self.__material = material

    def setTipo(self, tipo: str):
        self.__tipo = tipo

 
    def __str__(self):
        return f"Nombre: {self.nombre}, Material: {self.__material}, Tipo: {self.__tipo}"


def mostrar(instr: Instrumento):
    print(f"[Estructura] Nombre: {instr.nombre}, Material: {instr.getMaterial()}, Tipo: {instr.getTipo()}")

i1 = Instrumento("Desconocido", "", "")

i1.nombre = "Guitarra"
i1.setMaterial("Madera")
i1.setTipo("Cuerda")

print(i1)


print(f"Nombre: {i1.nombre}")
print(f"Material: {i1.getMaterial()}")
print(f"Tipo: {i1.getTipo()}")

i2 = Instrumento("Flauta", "Metal", "Aire")

print(i2)

print(f"Nombre: {i2.nombre}")
print(f"Material: {i2.getMaterial()}")
print(f"Tipo: {i2.getTipo()}")


mostrar(i1)
mostrar(i2)