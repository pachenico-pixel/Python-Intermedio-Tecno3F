from cuenta_bancaria import CuentaBancaria


class CuentaAhorro(CuentaBancaria):

    TASA_INTERES = 0.001

    def extraer(self, monto):
        if monto <= 0:
            raise ValueError("El monto debe ser mayor a cero.")

        if monto <= self.saldo:
            self.saldo -= monto
            print(f"Extracción exitosa: ${monto:.2f}")
        else:
            print("Saldo insuficiente.")

    def aplicar_interes(self):
        interes = self.saldo * self.TASA_INTERES
        self.saldo += interes
        print(f"Interés aplicado: ${interes:.2f}")