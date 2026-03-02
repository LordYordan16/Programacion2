class Televisor:
    def __init__(self, marca: str = "xd", resolucion: int = 0, tipo: str = ""):
        self.marca = marca
        self.resolucion = resolucion
        self.tipo = tipo


    def __str__(self):
        return f"Marca: {self.marca}, Resolución: {self.resolucion}p, Tipo: {self.tipo}"

tv1 = Televisor("Samsung", 1080, "OLED")
print(tv1)
tv2 = Televisor("LG", 720, "IPS")
print(tv2)
tv3 = Televisor()
print(tv3)