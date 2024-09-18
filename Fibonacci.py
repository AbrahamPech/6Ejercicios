class Fibonacci:

    def __init__(self):
        pass

    def main(self):
        numero = int(input("Introduce un numero para Fibonacci:"))
        resultado = self.fibonacci(numero)
        print(f"El número Fibonacci en la posición {numero} es: {resultado}")

    def fibonacci(self, n):  # Añadir self
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.fibonacci(n-1) + self.fibonacci(n-2)  # Añadir self
