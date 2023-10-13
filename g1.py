class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def mover(self):
        pass

class Mamifero(Animal):
    def amamantar(self):
        pass

class Ave(Animal):
    def volar(self):
        pass

class Perro(Mamifero):
    def mover(self):
        print(f"{self.nombre} camina")

class Gato(Mamifero):
    def mover(self):
        print(f"{self.nombre} camina")

class Pajaro(Ave):
    def mover(self):
        print(f"{self.nombre} vuela")

class Tortuga(Animal):
    def mover(self):
        print(f"{self.nombre} se arrastra")

# Crear instancias
fido = Perro("Fido")
whiskers = Gato("Whiskers")
tweety = Pajaro("Tweety")
slowpoke = Tortuga("Slowpoke")

# Ejemplos de uso
fido.mover()      # Fido camina
whiskers.mover()  # Whiskers camina
tweety.mover()    # Tweety vuela
slowpoke.mover()  # Slowpoke se arrastra
