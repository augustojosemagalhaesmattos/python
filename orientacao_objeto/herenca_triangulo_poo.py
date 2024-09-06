import math
import os

class Triangulo:
    def __init__(self, cateto_1, cateto_2):
        self.cateto_1 = cateto_1
        self.cateto_2 = cateto_2
        
        
        
class TrianguloRetangulo(Triangulo): # herança
    def calcular_hipotenusa(self):
        resultado = math.sqrt(pow(self.cateto_1, 2) + pow(self.cateto_2, 2))
        return resultado
    
    
while True:
    os.system('cls')
    cateto_1 = float(input('Entre com o cateto'))
        