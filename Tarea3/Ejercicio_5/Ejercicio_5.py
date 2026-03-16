from multimethod import multimethod

class Aula:
    def __init__(self, nombreAula: str, piso: int, estudiantes: list):
        self.__nombreAula = nombreAula
        self.__piso = piso
        self.__estudiantes = estudiantes

    @multimethod
    def mostrar(self):
        print(f"Nombre del Aula: {self.__nombreAula}")
        print(f"Piso: {self.__piso}")
        print("Estudiantes y Notas (sobre 100):")
        for estudiante in self.__estudiantes:
            print(f"Nombre: {estudiante[0]}, Nota: {estudiante[1]}")

    @multimethod
    def mostrar(self, estado: str):
        print(f"Nombre del Aula: {self.__nombreAula}")
        print("Estado de los estudiantes:")
        for estudiante in self.__estudiantes:
            nombre = estudiante[0]
            nota = estudiante[1]

            if nota >= 51:
                print(f"{nombre} - APROBADO")
            else:
                print(f"{nombre} - REPROBADO")

class Main:
    estudiantes = [("Juan", 85), ("María", 45), ("Pedro", 60)]
    aula = Aula("Matemáticas", 2, estudiantes)
    aula.mostrar()
    print()
    aula.mostrar("estado")
