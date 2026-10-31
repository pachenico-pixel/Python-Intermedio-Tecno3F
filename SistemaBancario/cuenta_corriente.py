from cuenta_bancaria import CuentaBancaria


class CuentaCorriente(CuentaBancaria):

    def __init__(self, titular, cbu, saldo, limite_descubierto=500):
        super().__init__(titular, cbu, saldo)
        self.limite_descubierto = limite_descubierto

    def extraer(self, monto):
        if monto <= 0:
            raise ValueError("El monto debe ser mayor a cero.")

        if monto <= self.saldo + self.limite_descubierto:
            # Se permite saldo negativo por el descubierto.
            # Se modifica internamente para respetar el setter
            # que impide asignar saldos negativos.
            self._saldo -= monto
            print(f"Extracción exitosa: ${monto:.2f}")
        else:
            print("Se superó el límite de descubierto.")