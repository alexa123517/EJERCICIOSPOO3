class Estudiante:
    def __init__(self, nombre, edad, calificacion):
        self.nombre = nombre
        self.edad = edad
        self.calificacion = calificacion

    def _estadoaprobacion(self):
        if self.calificacion >= 60:
            return f"{self.nombre} ha APROBADO con {self.calificacion}."
        else:
            return f"{self.nombre} ha REPROBADO con {self.calificacion}."

Estudiante1 = Estudiante("Alizardo", 22, 70)
Estudiante2 = Estudiante("Alexandra", 22, 55)

print(Estudiante1._estadoaprobacion())
print(Estudiante2._estadoaprobacion())
