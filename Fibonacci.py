import tkinter as tk
from tkinter import messagebox

class Fibonacci:

    def main(self, root):
        frame = tk.Frame(root)
        frame.pack(pady=20)

        tk.Label(frame, text="Introduce un número para Fibonacci (entre 1 y 35):").grid(row=0, column=0)
        numero_entry = tk.Entry(frame)
        numero_entry.grid(row=0, column=1)

        def calcular():
            try:
                numero = int(numero_entry.get())
                if numero > 35:
                    respuesta = messagebox.askyesno("Advertencia", "Un número mayor a 35 puede tardar en dar el resultado. ¿Estás seguro?")
                    if not respuesta:
                        return
                resultado = self.fibonacci(numero)
                messagebox.showinfo("Resultado", f"El número Fibonacci en la posición {numero} es: {resultado}")
            except ValueError:
                messagebox.showerror("Error", "Por favor, ingrese un número válido.")

        tk.Button(frame, text="Calcular", command=calcular).grid(row=1, columnspan=2, pady=10)

    def fibonacci(self, n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.fibonacci(n - 1) + self.fibonacci(n - 2)
