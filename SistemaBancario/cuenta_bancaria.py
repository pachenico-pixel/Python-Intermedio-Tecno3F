from abc import ABC, abstractmethod


class CuentaBancaria(ABC):

    def __init__(self, titular, cbu, saldo):
        self.titular = titular
        self._cbu = cbu
        self.saldo = saldo

    @property
    def cbu(self):
        return self._cbu

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        if valor < 0:
            raise ValueError("El saldo no puede ser negativo.")
        self._saldo = valor

    def depositar(self, monto):
        if monto <= 0:
            raise ValueError("El monto debe ser mayor a cero.")

        self._saldo += monto
        print(f"Depósito exitoso: ${monto:.2f}")

    def __str__(self):
        return (
            f"[{self.__class__.__name__}] "
            f"TITULAR: {self.titular} | "
            f"CBU: {self.cbu} | "
            f"SALDO: ${self.saldo:.2f}"
        )

    @abstractmethod
    def extraer(self, monto):
        pass