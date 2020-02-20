#Creando Clases
import math

class Calculadora:
    def __init__(self): #self es el this en java
        self.a = 0
        self.b = 0
        self.r = 0
    def suma(self):
        self.r = self.a+self.b
    def resta(self):
        self.r = self.a-self.b
    def multiplicacion(self):
        self.r = self.a*self.b
    def division(self):
        self.r = self.a/self.b
    def potencia(self):
        self.r = math.pow(self.a,self.b)
    def raiz(self):
        self.r = math.sqrt(self.a)
c = Calculadora()
c.a = 10
c.b = 20

c.suma()
print(c.r)
c.resta()
print(c.r)
c.division()
print(c.r)
c.multiplicacion()
print(c.r)
c.potencia()
print(c.r)
c.raiz()
print(c.r)
