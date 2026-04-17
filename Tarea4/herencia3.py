class Persona:
    def __init__(self, nombre, carnet, edad):
        self._nombre = nombre
        self._carnet = carnet
        self._edad = edad
    def __str__(self):
        return f"nombre: {self._nombre}, carnet: {self._carnet}, edad: {self._edad}"
   
class Estudiante(Persona):
    def __init__(self, nombre, carnet, edad, matricula, carrera):
        super().__init__(nombre, carnet, edad)
        self.__carrera = carrera
        self.__matricula = matricula
    def __str__(self):
        return super().__str__() + f" matricula: {self.__matricula}, carrera: {self.__carrera}"
    def verificarEdad(self, other: Persona):
        if (self._edad == other._edad) :
            return True
        else:
            return False
    def verificarCarrera(self, otro: Estudiante):
        if (self.__carrera == otro.__carrera):
            return True
        else:
            False
class Docente(Persona):
    def __init__(self, nombre, carnet, edad, antiguedad, sueldo):
        super().__init__(nombre, carnet, edad)
        self.__sueldo = sueldo
        self.__antiguedad = antiguedad
    def __str__(self):
        return super().__str__() + f" antiguedad: {self.__antiguedad}, sueldo: {self.__sueldo}"
    def verificarEdad(self, other: Persona):
        if (self._edad == other._edad) :
            return True
        else:
            return False
        
e1 = Estudiante("Roy", 123125, 19, 14900, "informatica")
e2 = Estudiante("Maria", 1136135, 45, 14125, "informatica")
d1 = Docente("Lyan", 124515, 45, 10, 3000)
print(e1)
print(e2)
print(d1)
print(e1.verificarEdad(d1))
print(e2.verificarEdad(d1))
print(e1.verificarCarrera(e2))