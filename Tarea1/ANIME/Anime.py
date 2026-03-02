class Anime:

    # Constructor
    def __init__(self, nombre, genero, nroEpisodios):
        self.nombre = nombre
        self.genero = genero
        self.__nroEpisodios = nroEpisodios
        self.__episodios = []

    
    def __str__(self):
         return f"Nombre: {self.nombre}, Género: {self.genero}, Episodios: {self.__nroEpisodios}"
    
a1 = Anime("Naruto", "Shonen", 220)
a2 = Anime("Death Note", "Suspenso", 37)

print(a1)
print(a2)