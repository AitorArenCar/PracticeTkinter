'''Completar donde se indica con #, de acuerdo a la siguiente consigna:
Utilizá las operaciones matemáticas más apropiada para obtener, del número 16823,
Sólo el último dígito (el 3)
Los dos últimos dígitos (el 23)
Los 3 últimos dígitos (el 823)
Todos los dígitos, excepto el último (1682)
El primer dígito (el 1)
Los dos primeros dígitos (el 16)
''' 

class Operaciones:
    def __init__(self, ventana):
        self.ventana=ventana

		
    def ultimoDigito(self):
        r= 16823 % 10   #completar con la instrucción necesaria para que la variable r guarde el último dígito de 16823
        self.ventana.resultado.configure(text=r)

    def dosUltimos(self):
        r= 16823 % 100   #completar con la instrucción necesaria para que la variable r guarde los dos últimos dígitos de 16823
        self.ventana.resultado.configure(text=r)

    def tresUltimos(self):
        r= 16823 % 1000   #completar con la instrucción necesaria para que la variable r guarde los tres últimos dígitos de 16823
        self.ventana.resultado.configure(text=r)

    def exceptoUltimo(self):
        r= 16823 // 10   #completar con la instrucción necesaria para que la variable r guarde todos los dígitos de 16823, excepto el último
        self.ventana.resultado.configure(text=r)

    def primerDigito(self):
        r= 16823 // 10000   #completar con la instrucción necesaria para que la variable r guarde el primer dígito de 16823
        self.ventana.resultado.configure(text=r)

    def primerosDos(self):
        r= 16823 // 1000   #completar con la instrucción necesaria para que la variable r guarde los dos primeros dígitos de 16823
        self.ventana.resultado.configure(text=r)
