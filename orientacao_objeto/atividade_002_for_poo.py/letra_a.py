# Faça um programa que imprima os números no intervalo
# entre 1 e 100. Os números devem ser apresentados na horizontal.

import os


class Intervalo:
    def __init__(self, numero):
        self.numero = numero
        
class imprimir(Intervalo):
    def calcular_intervalo(self):
     for i in range(self.numero + 1):
         print(f'{i}', end= " | ")
print
os.system('cls')
intervalo = imprimir(1, 100)
intervalo.calcular_intervalo()

    
                
       
    
        
  
    