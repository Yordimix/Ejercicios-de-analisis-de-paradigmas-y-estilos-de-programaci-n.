#Logica
#pip install z3-solver para que funcione...
from z3 import *

def main():
    a = Int('a')
    b = Int('b')

    solver = Solver()
    solver.add(a >= 0, a < 10)
    solver.add(b >= 0, b < 10)
    solver.add(a + b == 10)

    if solver.check() == sat:
        modelo = solver.model()
        print(f"a = {modelo[a]}, b = {modelo[b]}")
    else:
        print("No hay solución")

if __name__ == "__main__":
  main()