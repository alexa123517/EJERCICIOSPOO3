class Rectangulo:
    def _init_(self, largo, ancho):
        if largo > 0 and ancho > 0:
            self.__largo = largo
            self.__ancho = ancho
        else:
            raise ValueError("El largo y el ancho deben ser mayores que cero.")
    
    def cambiar_dimensiones(self, nuevo_largo, nuevo_ancho):
        if nuevo_largo > 0 and nuevo_ancho > 0:
            self.__largo = nuevo_largo
            self.__ancho = nuevo_ancho
        else:
            raise ValueError("Las nuevas dimensiones deben ser mayores que cero.")
    
    def calcular_area(self):
        return self._largo * self._ancho
    
    def calcular_perimetro(self):
        return 2 * (self._largo + self._ancho)
    
    def obtener_dimensiones(self):
        return self._largo, self._ancho


rectangulo = Rectangulo(5, 3)
print("Dimensiones iniciales:", rectangulo.obtener_dimensiones())
print("Área:", rectangulo.calcular_area())
print("Perímetro:", rectangulo.calcular_perimetro())
rectangulo.cambiar_dimensiones(7, 4)
print("Nuevas dimensiones:", rectangulo.obtener_dimensiones())
