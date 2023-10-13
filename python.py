# caso=[t for t in range(3) for i in range(3) for j in range(4) for k in range(5)]
# print(caso)
# class Padre:
#     def __init__(self, nombre):
#         self.nombre = nombre
#     def presentacion(self):
#         print("Hola soy", self.nombre)
# class Hijo(Padre):
#     def __init__(self, nombre, edad):
#         super().__init__(nombre)
#         self.edad = edad
#     def presentacion(self):
#         super().presentacion()
#         print("y tengo", self.edad, "anios")
# p = Padre("Juan")
# p.presentacion()
# h = Hijo("Pedro", 25)
# h.presentacion()
# print(isinstance(h, Padre))
class Padre:
    def __init__(self, nombre, **kwargs):
        self.nombre = nombre
    def presentacion(self):
        print("Hola soy", self.nombre)    
class Hijo(Padre):
    def __init__(self, nombre, edad, **kwargs):
        Padre.__init__(self, nombre, **kwargs)
        self.edad = edad
    def presentacion(self):
        super().presentacion()
        print("y tengo", self.edad, "anios, y mi padre es ", self.nombre)