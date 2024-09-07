# Faça um programa que imprima os números pares entre 0 e 100.

import os

os.system('cls')

class Numeros_Pares:
    def __init__(self, pares):
        self.pares = pares
    
class Numeros(Numeros_Pares):
    def numeros_pares(self):
        for i in range(1, 101):
            if i % 2 == 0:
                print(i)
            
pares = Numeros()
            
            
        
