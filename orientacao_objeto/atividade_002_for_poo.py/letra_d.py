# Faça um programa que imprima os números pares entre 0 e 100.

import os

os.system('cls')

class Numeros_Pares:
    def __init__(self, numero, final):
        self.numero = numero
        self.final = final

    def imprimir_numeros(self, numero, final):
       pass
    
class Numeros(Numeros_Pares):
    # def __init__(self, numero, final):
    #     self.numero = numero
    #     self.final = final
    
    def imprimir_numeros(self):
        
       for numero in range(self.numero, self.final):
          if numero % 2 == 0:
            print(numero, end= ' | ')
            soma += numero
        
            
os.system('cls')
numeros_pares = Numeros(0, 101)
numeros_pares.imprimir_numeros()



                
            
            

            
            
        
