from cuenta_bancaria import CuentaBancaria


class CuentaCheque(CuentaBancaria):

    def __init__(self, titular, cbu, saldo, costo_emision=50):
        super().__init__(titular, cbu, saldo)
        self.costo_emision = costo_emision

    def extraer(self, monto):
        if monto <= 0:
            raise ValueError("El monto debe ser mayor a cero.")

        total = monto + self.costo_emision

        if total <= self.saldo:
            self.saldo -= total
            print(f"Extracción exitosa: ${monto:.2f}")
            print(f"Comisión: ${self.costo_emision:.2f}")
            print(f"Total descontado: ${total:.2f}")
        else:
            print("Saldo insuficiente para cubrir la extracción y comisión.")