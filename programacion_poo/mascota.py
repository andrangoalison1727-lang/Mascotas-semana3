class Mascota:
    def __init__(self, especie, nombre, edad):
        self.especie = especie
        self.nombre = nombre
        self.edad = edad
    def mostrar_informacion(self):
        print(f"Especie: {self.especie}")
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
    def hacer_sonido(self):
        print(f"{self.nombre} emite un sonido de su especie.")
