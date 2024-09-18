class Factorial:

    def __init__(self):
        pass

    def main(self):
        numero = int(input("Ingrese un numero a factorizar:"))
        resultado = self.FactorialRecursivo(numero)
        print("El resultado de " + str(numero) + " es igual a " + str(resultado))

    def FactorialRecursivo(self, n):
        if n == 0 or n == 1:
            return 1
        else:
            return n * self.FactorialRecursivo(n - 1)

    def AlgoRecursivo(self, n):
        print(n)
        if n > 0:
            return self.AlgoRecursivo(n - 1)
        else:
            return 0

    @staticmethod
    def Factorial(n):
        fact = 1
        for i in range(1, n + 1):
            fact *= i
        return fact
