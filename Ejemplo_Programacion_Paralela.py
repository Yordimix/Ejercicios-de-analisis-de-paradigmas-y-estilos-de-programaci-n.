# Paralelo
import threading

def tarea(id):
    print(f"Tarea {id} iniciada.")
    print(f"Tarea {id} completada.")

def main():
    hilos = []
    for i in range(5):
        hilo = threading.Thread(target=tarea, args=(i,))
        hilos.append(hilo)
        hilo.start()

    for hilo in hilos:
        hilo.join()

if __name__ == "__main__":
    main()
