
class TorreDeHanoi:
    def __init__(self):
        self.movimientos = []

    def resolver_hanoi(self, n, origen, destino, auxiliar):
        if n == 1:
            self.movimientos.append((n, origen, destino))
        else:
            self.resolver_hanoi(n - 1, origen, auxiliar, destino)
            self.movimientos.append((n, origen, destino))
            self.resolver_hanoi(n - 1, auxiliar, destino, origen)

    def mostrar_movimientos(self):
        for movimiento in self.movimientos:
            ficha, desde, hacia = movimiento
            print(f"Ficha {ficha} de {desde} a {hacia}")

    def main(self):
        try:
            n = int(input("Introduce el número de fichas: "))
            if n <= 0:
                print("El número de fichas debe ser mayor que 0.")
                return

            self.resolver_hanoi(n, 'A', 'C', 'B')
            self.mostrar_movimientos()
        except ValueError:
            print("Por favor, introduce un número entero válido.")