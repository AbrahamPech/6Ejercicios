import tkinter as tk
from tkinter import messagebox

class Factorial:

    def main(self, root):
        frame = tk.Frame(root)
        frame.pack(pady=20)
        tk.Label(frame, text="Ingrese un número a factorizar:").grid(row=0, column=0)
        numero_entry = tk.Entry(frame)
        numero_entry.grid(row=0, column=1)


        def calcular():
            try:
                numero = int(numero_entry.get())  # Convertir el valor del Entry a entero
                if numero < 0:
                    messagebox.showerror("Error", "El número a factorizar debe ser mayor o igual a 0.")
                    return
                resultado = self.FactorialRecursivo(numero)
                messagebox.showinfo("Resultado", f"El resultado de {numero} es igual a {resultado}")
            except ValueError:
                messagebox.showerror("Error", "Por favor, ingrese un número válido.")

        tk.Button(frame, text="Calcular", command=calcular).grid(row=1, columnspan=2, pady=10)

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
