# Funcional
from functools import reduce

def suma(a, b):
    return a + b

def main():
    lista = [1, 2, 3, 4, 5]
    resultado = reduce(suma, lista)
    print(f"La suma de la lista es {resultado}")

if __name__ == "__main__":
    main()
