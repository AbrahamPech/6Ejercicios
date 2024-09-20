import time
class N_Reinas:
    def __init__(self):
        self.soluciones = []

    def es_valido(self, tablero, fila, col, n):
        # Verifica si hay alguna reina en la misma columna
        for i in range(fila):
            if tablero[i] == col:
                return False

        # Verifica la diagonal superior izquierda
        for i, j in zip(range(fila, -1, -1), range(col, -1, -1)):
            if tablero[i] == j:
                return False

        # Verifica la diagonal superior derecha
        for i, j in zip(range(fila, -1, -1), range(col, n)):
            if tablero[i] == j:
                return False

        return True

    def resolver_n_reinas(self, tablero, fila, n):
        # Si se han colocado todas las reinas, la solución es válida
        if fila == n:
            self.soluciones.append(tablero[:])
            return

        # Intenta colocar una reina en cada columna de la fila actual
        for col in range(n):
            if self.es_valido(tablero, fila, col, n):
                tablero[fila] = col  # Coloca la reina en la columna actual
                self.resolver_n_reinas(tablero, fila + 1, n)  # Intenta colocar la siguiente reina
                tablero[fila] = -1  # Elimina la reina y retrocede (backtracking)

    def imprimir_solucion(self, solucion, n):
        # Imprime una solución en formato visual de tablero
        for i in range(n):
            fila = ['.'] * n
            fila[solucion[i]] = 'Q'  # Coloca la reina en la posición correspondiente
            print(' '.join(fila))
        print("Solución número:", self.soluciones.index(solucion) + 1)
        time.sleep(1)

    def main(self):
        # Solicitar el valor de N (tamaño del tablero)
        try:
            n = int(input("Introduce el tamaño del tablero (mayor a 3): "))
        except ValueError:
            print("Por favor, introduce un número válido.")
            return

        # Inicializa el tablero (usando una lista donde el índice es la fila y el valor es la columna)
        tablero = [-1] * n

        # Resuelve el problema de N reinas
        self.resolver_n_reinas(tablero, 0, n)

        # Muestra las soluciones encontradas
        print(f"Se encontraron {len(self.soluciones)} soluciones para un tablero de {n}x{n}:\n")
        for solucion in self.soluciones:
            self.imprimir_solucion(solucion, n)