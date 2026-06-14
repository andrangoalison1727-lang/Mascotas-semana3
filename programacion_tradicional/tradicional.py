#Registrar y mostrar datos de una mascota
def registrar_mascota(especie, nombre, edad):
    mascota = {
        "especie" : especie,
        "nombre" : nombre,
        "edad" : edad,
        }
    return mascota
def mostrar_mascota(mascota):
    print(f"especie: {mascota['especie']}")
    print(f"nombre: {mascota['nombre']}")
    print(f"edad: {mascota['edad']} años")

#Solicitar datos de la mascota
especie = input("Especie de la mascota: ")
nombre = input("Nombre de la mascota: ")
edad = input("Edad de la mascota: ")

#registrar y mostrar datos de la mascota
mascota = registrar_mascota(especie, nombre, edad)
mostrar_mascota(mascota)
