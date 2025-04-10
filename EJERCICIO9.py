class Estudiante:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad
        self.__notas = []

    def agregar_nota(self, nota):
        if 0 <= nota <= 100:
            self.__notas.append(nota)
        else:
            raise ValueError("La nota debe estar entre 0 y 100.")

    def calcular_promedio(self):
        if not self.__notas:
            return 0
        return sum(self.__notas) / len(self.__notas)

    def obtener_nombre(self):
        return self.__nombre

    def obtener_edad(self):
        return self.__edad



if __name__ == "main":
    try:
        estudiante = Estudiante("Alexandra Almanza", 20)
        estudiante.agregar_nota(90)
        estudiante.agregar_nota(93)
        estudiante.agregar_nota(79)

        print(f"Nombre: {estudiante.obtener_nombre()}")
        print(f"Edad: {estudiante.obtener_edad()}")
        print(f"Promedio de notas: {estudiante.calcular_promedio():.2f}")

      
    except ValueError as e:
        print(f"Error: {e}")
