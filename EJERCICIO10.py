class Libro:
    def __init__(self, titulo, autor, total_paginas):
        self.__titulo = titulo
        self.__autor = autor
        if total_paginas > 0:
            self.__total_paginas = total_paginas
        else:
            raise ValueError("El número total de páginas debe ser mayor a 0.")
        self.__pagina_actual = 1

    def avanzar_paginas(self, paginas):
        if self.__pagina_actual + paginas > self.__total_paginas:
            raise ValueError("No se puede avanzar más allá del final del libro.")
        self.__pagina_actual += paginas

    def retroceder_paginas(self, paginas):
        if self.__pagina_actual - paginas < 1:
            raise ValueError("No se puede retroceder más allá de la página 1.")
        self.__pagina_actual -= paginas

    def obtener_pagina_actual(self):
        return self.__pagina_actual

    def obtener_info_completa(self):
        return (f"Título: {self.__titulo}\n"
                f"Autor: {self.__autor}\n"
                f"Total de páginas: {self.__total_paginas}\n"
                f"Página actual: {self.__pagina_actual}")


if __name__ == "__main__":
    try:
        libro = Libro("1986", "Juan Gabriel Marquez", 328)
        print(libro.obtener_info_completa())

        libro.avanzar_paginas(30)
        print(f"\nPágina actual: {libro.obtener_pagina_actual()}")

        libro.retroceder_paginas(10)
        print(f"Página actual tras retroceder: {libro.obtener_pagina_actual()}")

     
    except ValueError as e:
        print(f"Error: {e}")
