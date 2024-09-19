class Fibonacci:

    def __init__(self):
        pass

    def main(self):
        while True:
            numero = int(input("Introduce un número para Fibonacci (entre 1 y 35): "))
            if numero > 35:
                respuesta = input("Un número mayor a 35 puede tardar en dar el resultado. ¿Estás seguro?\n1.- Sí\n2.- No\nRespuesta: ")
                if respuesta == '1':
                    break
                elif respuesta == '2':
                    continue
                else:
                    input("Respuesta no válida, vuelva a seleccionar el número que quiere en Fibonacci.")
                    continue  # Volver a pedir el número
            else:
                break  # Si el número es válido, sale del ciclo
        
        resultado = self.fibonacci(numero)
        print(f"El número Fibonacci en la posición {numero} es: {resultado}")

    def fibonacci(self, n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.fibonacci(n - 1) + self.fibonacci(n - 2)
