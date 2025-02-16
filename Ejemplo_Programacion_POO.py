# Programación orientada a objetos
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola, me llamo {self.nombre} y tengo {self.edad} años.")

def main():
    persona = Persona("Juan", 30)
    persona.saludar()

if __name__ == "__main__":
    main()
