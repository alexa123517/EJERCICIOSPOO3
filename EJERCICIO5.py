class CuentaBancaria:
    def _init_(self, titular, saldo=0):
        self.__titular = titular
        self.__saldo = saldo if saldo >= 0 else 0
    
    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
        else:
            raise ValueError("La cantidad a depositar debe ser mayor que cero.")
    
    def retirar(self, cantidad):
        if 0 < cantidad <= self.__saldo:
            self.__saldo -= cantidad
        else:
            raise ValueError("Fondos insuficientes o cantidad inválida.")
    
    def consultar_saldo(self):
        return self.__saldo
    
    def obtener_titular(self):
        return self.__titular

class CuentaAhorro(CuentaBancaria):
    def _init_(self, titular, saldo=0, interes_anual=0):
        super()._init_(titular, saldo)
        if interes_anual >= 0:
            self.__interes_anual = interes_anual
        else:
            raise ValueError("El interés anual no puede ser negativo.")
    
    def aplicar_interes(self):
        nuevo_saldo = self.consultar_saldo() * (1 + self.__interes_anual / 100)
        self.depositar(nuevo_saldo - self.consultar_saldo())
    
    def consultar_interes(self):
        return self.__interes_anual


cuenta = CuentaAhorro("Jose", 1000, 5)
print("Titular:", cuenta.obtener_titular())
print("Saldo inicial:", cuenta.consultar_saldo())
cuenta.aplicar_interes()
print("Saldo después de aplicar interés:", cuenta.consultar_saldo())
