class MCD:
    def __init__(self):
        pass
    
    def calcular_mcd(self, a, b):
        # Método recursivo para calcular el MCD
        if b == 0:
            return a
        else:
            return self.calcular_mcd(b, a % b)
    
    def main(self):
        try:
            a = int(input("Introduce el primer número: "))
            b = int(input("Introduce el segundo número: "))
            resultado = self.calcular_mcd(a, b)
            print(f"El MCD de {a} y {b} es: {resultado}")
        except ValueError:
            print("Por favor, introduce números enteros válidos.")
