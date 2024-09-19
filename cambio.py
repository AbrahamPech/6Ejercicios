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

    def main(self):
        # Solicita al usuario dos números y muestra el cambio
        try:
            total_pagar = float(input("Ingrese el total a pagar: "))
            cantidad_pagada = float(input("Ingrese la cantidad pagada: "))
            
            if cantidad_pagada < total_pagar:
                print("La cantidad pagada debe ser mayor o igual al total a pagar.")
            else:
                cambio = self.calcular_cambio(total_pagar, cantidad_pagada)
                print("El cambio a devolver es:")
                for denominacion, cantidad in cambio.items():
                    print(f"{cantidad} {denominacion}")
        except ValueError:
            print("Por favor, ingrese un número válido.")
