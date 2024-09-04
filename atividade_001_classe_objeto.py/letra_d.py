# Faça um programa que receba e divida 2 números. 
# A saída da divisão precisará ser formatada com 4 casas decimais.

import os


class Divisao:
    def __init__ (self,numero1, numero2):
        self.numero1 = numero1
        self.numero2 = numero2
    
    def divisao(self):
      resultado = self.numero1 / self.numero2
      return resultado
        
os.system('cls')
numero1 = int(input('Digite o 1º numero: '))
numero2 = int(input('Digite o 2º numero: '))

divisao1 = Divisao(numero1, numero2)
resultado_divisao = divisao1.divisao()

print('-'*70)
print(f'A Divisao é {resultado_divisao}')


    
    

        
        
    
    
