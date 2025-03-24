class Libro:
    def __init__(self, titulo, autor, num_paginas):  # Corregido el constructor
        self.titulo = titulo
        self.autor = autor
        self.num_paginas = num_paginas
    
    def mostrar_info(self):
        print(f"Título: {self.titulo}, Autor: {self.autor}, Páginas: {self.num_paginas}")
    
    def actualizar_paginas(self, nuevas_paginas):
        if nuevas_paginas > 0:
            self.num_paginas = nuevas_paginas
            print(f"El número de páginas ha sido actualizado a {self.num_paginas}")
        else:
            print("El número de páginas debe ser mayor a 0.")
            
libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", 471)
libro1.mostrar_info()
libro1.actualizar_paginas(500)
