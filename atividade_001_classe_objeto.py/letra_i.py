# Faça um programa que receba um valor em reais,
# depois calcule quantos dólares daria para comprar com esse valor.

import os


class Conversao:
    def __init__ (self, valor):
        self.valor = valor
    
    def dolares(self):
       converter = self.valor * 5
       return converter
   
os.system('cls')
valor = int(input('Digite um valor: '))

conversao = Conversao(valor)
resultado = conversao.dolares()

print('-'*70)
print(f'{valor} reais convertendo em dolares é:{resultado}')
print('-'*70)


