# Faça um programa que receba um número inteiro,
# depois imprima sua tabuada de multiplicação.

import os


class Tabuada:
    def __init__ (self,numero):
        self.numero = numero
    
    def multiplicar(self, multiplicador):
        tabuada = []
        for i in range(1, 11):
            tabuada.append(multiplicador * i)
        return tabuada
            
        
os.system('cls')
numero = int(input('Digite um número: '))

tabuada = Tabuada(numero)
resultados = tabuada.multiplicar(numero)


print('-'*70)
for indice, numero in enumerate(resultados):
    print(f'{numero} * {indice+1} = {numero}')
    


        
    

