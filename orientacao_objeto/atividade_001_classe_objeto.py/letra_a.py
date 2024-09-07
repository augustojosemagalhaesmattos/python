# Faça um programa que peça 3 valores ,
# depois calcule e imprima  a soma e a multiplicação 
# desses valores. 

import os


class Calculadora:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        
    def somar(self):
        return self.a + self.b + self.c
    
    def multiplicacao(self):
        return self.a * self.b * self.c
    
os.system('cls')
print('-'*70)
a = int(input('Digite o 1º valor: '))
b = int(input('Digite o 2º valor: '))
c = int(input('Digite o 3º valor: '))

valores = Calculadora(a, b, c)

resultado_soma = valores.somar()
resultado_multiplicar = valores.multiplicacao()

print('='*70)
print(f'Soma dos tres valores: {resultado_soma}')
print('='*70)
print(f'Multiplicação dos tres valores: {resultado_multiplicar}')
print('='*70)
