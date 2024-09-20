import tkinter as tk
from tkinter import messagebox
from Factorizacion import Factorial
from Fibonacci import Fibonacci
from mcd import MCD
from cambio import Cambio
from TdH import TorreDeHanoi
from Reinas import N_Reinas

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Menú de Ejercicios")
        self.geometry("300x300")
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="Selecciona un ejercicio").pack(pady=10)
        
        tk.Button(self, text="Factorial", command=self.run_factorial).pack(pady=5)
        tk.Button(self, text="Fibonacci", command=self.run_fibonacci).pack(pady=5)
        tk.Button(self, text="MCD", command=self.run_mcd).pack(pady=5)
        tk.Button(self, text="Cambio de Monedas", command=self.run_cambio).pack(pady=5)
        tk.Button(self, text="Torre de Hanoi", command=self.run_hanoi).pack(pady=5)
        tk.Button(self, text="N Reinas", command=self.run_reinas).pack(pady=5)
        tk.Button(self, text="Salir", command=self.quit).pack(pady=5)

    def run_factorial(self):
        self.new_window(Factorial)

    def run_fibonacci(self):
        self.new_window(Fibonacci)

    def run_mcd(self):
        self.new_window(MCD)

    def run_cambio(self):
        self.new_window(Cambio)

    def run_hanoi(self):
        self.new_window(TorreDeHanoi)

    def run_reinas(self):
        self.new_window(N_Reinas)

    def new_window(self, cls):
        new_win = tk.Toplevel(self)
        new_win.geometry("300x300")
        cls().main(new_win)

if __name__ == "__main__":
    app = App()
    app.mainloop()
