import tkinter as tk
from tkinter import messagebox

class MCD:
    def main(self, root):
        frame = tk.Frame(root)
        frame.pack(pady=20)

        tk.Label(frame, text="Introduce el primer número:").grid(row=0, column=0)
        a_entry = tk.Entry(frame)
        a_entry.grid(row=0, column=1)

        tk.Label(frame, text="Introduce el segundo número:").grid(row=1, column=0)
        b_entry = tk.Entry(frame)
        b_entry.grid(row=1, column=1)

        def calcular():
            try:
                a = int(a_entry.get())
                b = int(b_entry.get())
                resultado = self.calcular_mcd(a, b)
                messagebox.showinfo("Resultado", f"El MCD de {a} y {b} es: {resultado}")
            except ValueError:
                messagebox.showerror("Error", "Por favor, ingrese números válidos.")

        tk.Button(frame, text="Calcular", command=calcular).grid(row=2, columnspan=2, pady=10)

    def calcular_mcd(self, a, b):
        if b == 0:
            return a
        else:
            return self.calcular_mcd(b, a % b)
