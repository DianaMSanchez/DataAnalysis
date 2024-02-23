import tratamiento as t
import app


def showMenu():
    print()
    print()        
    print("Selecciona una de las opciones:")
    print()
    print("1. Muestra restaurantes por PAIS")
    print("2. Muestra restaurantes por GESTION DE PROPIETARIO")
    print("0. Salir")

def ejecutarOption(opcion):
    if opcion ==1:
        t.restByCountry()
    if opcion ==2:
        t.restByClaimed()            
    if opcion == 0:
        exit()

if __name__ == "__main__":
    opcion = -1

    while opcion != 0:
        showMenu()
        try:
            opcion = int(input())
            ejecutarOption(opcion)
        except ValueError:
            print("Opción no válida. Introduzca nuevo valor: ")