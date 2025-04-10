class TarjetaCredito:
    def __init__(self, numero):
        self.numero = numero
    
    @staticmethod
    def validar_tarjeta(numero):
       
        numero = str(numero)[::-1]
        
        suma = 0
        
        for i, digito in enumerate(numero):
            digito = int(digito)
            
           
            if i % 2 == 1:
                digito *= 2
               
                if digito > 9:
                    digito -= 9
            
            suma += digito
        
       
        return suma % 10 == 0


numero_tarjeta = 1234567812345670
if TarjetaCredito.validar_tarjeta(numero_tarjeta):
    print("La tarjeta es válida.")
else:
    print("La tarjeta no es válida.")
