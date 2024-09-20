import time
import tkinter as tk
from tkinter import messagebox

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
        resultado = ""
        for movimiento in self.movimientos:
            ficha, desde, hacia = movimiento
            resultado += f"Ficha {ficha} de {desde} a {hacia}\n"
        return resultado

    def main(self, root):
        frame = tk.Frame(root)
        frame.pack(pady=20)

        tk.Label(frame, text="Introduce el número de fichas:").grid(row=0, column=0)
        n_entry = tk.Entry(frame)
        n_entry.grid(row=0, column=1)

        def calcular():
            try:
                n = int(n_entry.get())
                if n <= 0:
                    messagebox.showerror("Error", "El número de fichas debe ser mayor que 0.")
                    return
                self.movimientos = []
                self.resolver_hanoi(n, 'A', 'C', 'B')
                resultado = self.mostrar_movimientos()
                
                # Crear una nueva ventana para mostrar los resultados con scrollbar
                result_window = tk.Toplevel(root)
                result_window.title("Movimientos")
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