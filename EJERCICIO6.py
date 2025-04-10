class Empleado:
    __contador_empleados = 0  

    def _init_(self, nombre, salario):
        self.__nombre = nombre
        self.__salario = salario
        Empleado.__contador_empleados += 1  
    
    def obtener_nombre(self):
        return self.__nombre
    
    def obtener_salario(self):
        return self.__salario
    
    @classmethod
    def cantidad_empleados(cls):
        return cls.__contador_empleados


empleado1 = Empleado("Maria", 3000)
empleado2 = Empleado("Carlos", 3500)
print("Total de empleados:", Empleado.cantidad_empleados())
