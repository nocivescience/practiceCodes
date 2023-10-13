class Animal:
    def __init__(self, nombre, direccion=None):
        if direccion is None:
            direccion = ['noreste', 'noroeste', 'sureste', 'suroeste']
        self.nombre = nombre
        self.direccion = direccion
        print (f"Animal {self.nombre} creado con direccion {self.direccion}")

    def mover(self):
        anuncio = f"{self.nombre} se mueve"
        return anuncio

class Mamifero(Animal):
    def amamantar(self):
        print ('madre amamanta a su cria')

class Ave(Animal):
    def volar(self):
        return print('este vuela caleta')

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

fido.amamantar()      # Fido camina
animal1= Animal('Sorco')
animal1.mover()
ave1= Ave('Pajaro')
ave1.volar()