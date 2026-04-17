import math
class Figura:
    def __init__(self, color):
        self._color = color
    def _obtenerArea(self):
        pass
    def __str__(self):
        return f"color: {self._color}"
    def mayorArea(self, otro: Figura):
        if (self._obtenerArea() > otro._obtenerArea()):
            return self._color
        else:
            return otro._color
class Cuadrado(Figura):
    def __init__(self, color, lado):
        super().__init__(color)
        self.__lado = lado
    def _obtenerArea(self):
        return self.__lado**2
    def __str__(self):
        return super().__str__() + f" lado: {self.__lado}"
    def mayorArea(self, otro):
        return super().mayorArea(otro)
class Triangulo(Figura):
    def __init__(self, color, lado1, lado2, lado3):
        super().__init__(color)
        self.__lado1 = lado1
        self.__lado2 = lado2
        self.__lado3 = lado3
    def _obtenerArea(self):
        if (self.__lado1 == self.__lado2):
            return (self.__lado1 * self.__lado3)/2
        elif(self.__lado1 == self.__lado3):
            return (self.__lado1 * self.__lado2)/2
        elif(self.__lado2 == self.__lado3):
            return (self.__lado1 * self.__lado3)/2
        else:
            p = (self.__lado1 + self.__lado2 + self.__lado3)/2
            return math.sqrt(p*(p-self.__lado1)*(p-self.__lado2)*(p-self.__lado3))
    def __str__(self):
        return super().__str__() + f" lado1: {self.__lado1}, lado2: {self.__lado2}, lado3: {self.__lado3}"
    def mayorArea(self, otro):
        return super().mayorArea(otro)
class Redondo(Figura):
    def __init__(self, color, radio):
        super().__init__(color)
        self.__radio = radio
    def _obtenerArea(self):
        return math.pi*(self.__radio**2)
    def __str__(self):
        return super().__str__() + f" radio: {self.__radio}"
    def mayorArea(self, otro):
        return super().mayorArea(otro)
class Main:
    c1 = Cuadrado("dorado", 2)
    print(c1)
    c2 = Cuadrado("verde", 3)
    print(c2)
    t1 = Triangulo("negro", 2, 2, 3)
    print(t1)
    t2 = Triangulo("limon", 2, 4, 3)
    print(t2)
    r1 = Redondo("blanco", 3)
    print(r1)
    r2 = Redondo("oscuro", 5)
    print(r2)
    print(c2.mayorArea(t2))
