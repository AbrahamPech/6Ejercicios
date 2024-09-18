# Importacion de clases
from Factorizacion import Factorial
from Fibonacci import Fibonacci  # Corregir la importación
import os
# menu en python


while True:

    print("\nSeleciona un ejercicio\n 1.- Ejericicio:Factorial \n 2.- Ejericicio:Fibonacci\n 3.- Ejercicio:MCD\n 4.- Ejercicio:Cambio monedas\n 5.- Ejercicio:Torre de Hanòi\n 6.- Ejercicio:Propio\n 0.- Salir")

    opcion = input("Introduce un número: ")

    if opcion == '1':
        factorial = Factorial()
        factorial.main()
        
    elif opcion == '2':
        fibo = Fibonacci()  # Corregir la instancia de Fibonacci
        fibo.main()

    elif opcion == '3':
        print("Ejercicio de MCD no implementado aún.")

    elif opcion == '4':
        print("Ejercicio de Cambio de Monedas no implementado aún.")

    elif opcion == '5':
        print("Ejercicio de Torres de Hanói no implementado aún.")

    elif opcion == '6':
        print("Ejercicio propio no implementado aún.")

    elif opcion == '0':
        print("Saliendo del programa.")
        break

    else:
        print("Opción no válida, selecciona una de las indicadas.")

    input("Presione alguna tecla para continuar")
    os.system('cls')
