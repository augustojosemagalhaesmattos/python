# Faça um programa que receba um número inteiro
# e mostre o sucessor e antecessor.

import os


class Sucessor_Antecessor:
    def __init__ (self, numero):
        self.numero = numero
    
    def suceder (self):
        sucessor = self.numero + 1
        return sucessor
    
    def antecessor (self):
        antecessor =  self.numero - 1
        return antecessor
    
os.system('cls')
numero = int(input('Digite um número inteiro: '))

dados = Sucessor_Antecessor(numero)
resultado_antecessor = dados.antecessor()
resultado_suceder = dados.suceder()

print('-'*70)
print(f'Antecessor de {numero} é: {resultado_antecessor} ')
print(f'Sucessor de {numero} é: {resultado_suceder} ')
    
    
        
        
    
