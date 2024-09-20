import tkinter as tk
from tkinter import messagebox

class Cambio:
    @staticmethod
    def calcular_cambio(total_pagar, cantidad_pagada, denominaciones=None, resultado=None):
        if denominaciones is None:
            denominaciones = [
                (100, "monedas de 100 pesos"),
                (50, "monedas de 50 pesos"),
                (20, "monedas de 20 pesos"),
                (10, "monedas de 10 pesos"),
                (5, "monedas de 5 pesos"),
                (1, "monedas de 1 peso"),
                (0.5, "monedas de 50 centavos"),
                (0.2, "monedas de 20 centavos"),
                (0.01, "monedas de 1 centavo")
            ]
        
        if resultado is None:
            resultado = {}
        
        if not denominaciones:
            return resultado
        
        valor, nombre = denominaciones[0]
        cambio = cantidad_pagada - total_pagar
        valor_cents = round(valor * 100)
        cambio_cents = round(cambio * 100)
        cantidad_monedas = cambio_cents // valor_cents
        
        if cantidad_monedas > 0:
            resultado[nombre] = cantidad_monedas
            cantidad_pagada -= cantidad_monedas * valor
        
        return Cambio.calcular_cambio(total_pagar, cantidad_pagada, denominaciones[1:], resultado)

    def main(self, root):
        frame = tk.Frame(root)
        frame.pack(pady=20)

        tk.Label(frame, text="Total a pagar:").grid(row=0, column=0)
        total_pagar_entry = tk.Entry(frame)
        total_pagar_entry.grid(row=0, column=1)

        tk.Label(frame, text="Cantidad pagada:").grid(row=1, column=0)
        cantidad_pagada_entry = tk.Entry(frame)
        cantidad_pagada_entry.grid(row=1, column=1)

        def calcular():
            try:
                total_pagar = float(total_pagar_entry.get())  # Convierte el valor del Entry
                cantidad_pagada = float(cantidad_pagada_entry.get())  # Convierte el valor del Entry
                
                if total_pagar < 0:
                    messagebox.showerror("Error", "El total a pagar debe ser mayor o igual a 0.")
                    return

                if cantidad_pagada < total_pagar:
                    messagebox.showerror("Error", "La cantidad pagada debe ser mayor o igual al total a pagar.")
                else:
                    cambio = self.calcular_cambio(total_pagar, cantidad_pagada)
                    resultado = "\n".join([f"{cantidad} {denominacion}" for denominacion, cantidad in cambio.items()])
                    messagebox.showinfo("Cambio", f"El cambio a devolver es:\n{resultado}")
            except ValueError:
                messagebox.showerror("Error", "Por favor, ingrese un número válido.")

        tk.Button(frame, text="Calcular", command=calcular).grid(row=2, columnspan=2, pady=10)
