class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def verificar_disponibilidad(self, cantidad):
        if self.stock >= cantidad:
            return True
        else:
            return False
    def vender(self, cantidad):
        if self.verificar_disponibilidad(cantidad):
            self.stock -= cantidad
            print(f"Se han vendido {cantidad} unidades de {self.nombre}. Stock restante: {self.stock}.")
        else:
            print(f"No hay suficiente stock de {self.nombre}. Solo hay {self.stock} unidades disponibles.")
    def reabastecer(self, cantidad):
        self.stock += cantidad
        print(f"Se han reabastecido {cantidad} unidades de {self.nombre}. Stock actual: {self.stock}.")
producto = Producto("Laptop", 1200, 10)
if producto.verificar_disponibilidad(5):
    print("Hay suficientes unidades disponibles para vender 5 unidades.")
