# Faça um programa que converta metros em centímetros e milímetros.

import os


class Conversao:
    def __init__ (self, metros):
        self.metros = metros
    
    def centimetros(self):
       centimetros = self.metros * 100
       return centimetros
    
    def milimetros(self):
        milimetros = self.metros * 1000
        return milimetros
        
os.system('cls')
metros = int(input('Digite um número: '))

conversao = Conversao(metros)

resultado_milimetros = conversao.milimetros()
resultado_centimetros = conversao.centimetros()

print('-'*70)
print(f'{metros} convertendo para milimetros é: {resultado_milimetros} milimetros')
print(f'{metros} convertendo para centimetros é: {resultado_centimetros} centimetros')
print('-'*70)

    