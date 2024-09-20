import time
import tkinter as tk
from tkinter import messagebox

class N_Reinas:
    def __init__(self):
        self.soluciones = []

    def es_valido(self, tablero, fila, col, n):
        for i in range(fila):
            if tablero[i] == col:
                return False
        for i, j in zip(range(fila, -1, -1), range(col, -1, -1)):
            if tablero[i] == j:
                return False
        for i, j in zip(range(fila, -1, -1), range(col, n)):
            if tablero[i] == j:
                return False
        return True

    def resolver_n_reinas(self, tablero, fila, n):
        if fila == n:
            self.soluciones.append(tablero[:])
            return
        for col in range(n):
            if self.es_valido(tablero, fila, col, n):
                tablero[fila] = col
                self.resolver_n_reinas(tablero, fila + 1, n)
                tablero[fila] = -1

    def imprimir_solucion(self, solucion, n):
        for i in range(n):
            fila = ['.'] * n
            fila[solucion[i]] = 'Q'
            print(' '.join(fila))
        print("Solución número:", self.soluciones.index(solucion) + 1)
        time.sleep(1)

    def main(self, root):
        frame = tk.Frame(root)
        frame.pack(pady=20)

        tk.Label(frame, text="Introduce el tamaño del tablero (mayor a 3):").grid(row=0, column=0)
        n_entry = tk.Entry(frame)
        n_entry.grid(row=0, column=1)

        def calcular():
            try:
                n = int(n_entry.get())
                if n <= 3:
                    messagebox.showerror("Error", "El tamaño del tablero debe ser mayor a 3.")
                    return
                tablero = [-1] * n
                self.soluciones = []  # Reset solutions
                self.resolver_n_reinas(tablero, 0, n)
                resultado = f"Se encontraron {len(self.soluciones)} soluciones para un tablero de {n}x{n}:\n"
                for solucion in self.soluciones:
                    resultado += "\n".join([' '.join(['Q' if i == col else '.' for i in range(n)]) for col in solucion]) + "\n\n"
                # Crear una nueva ventana para mostrar los resultados con scrollbar
                result_window = tk.Toplevel(root)
                result_window.title("Soluciones")
                text_area = tk.Text(result_window, wrap=tk.WORD)
                scrollbar = tk.Scrollbar(result_window, command=text_area.yview)
                text_area.config(yscrollcommand=scrollbar.set)
                text_area.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
                scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
                text_area.insert(tk.END, resultado)
                text_area.config(state=tk.DISABLED)
            except ValueError:
                messagebox.showerror("Error", "Por favor, ingrese un número válido.")

        tk.Button(frame, text="Calcular", command=calcular).grid(row=1, columnspan=2, pady=10)