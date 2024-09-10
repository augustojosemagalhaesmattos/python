# Faça um programa que peça 3 valores ,
# depois calcule e imprima  a soma e a multiplicação 
# desses valores. 

import os


class Calcular:
    def __init__(self, valor1, valor2, valor3):
        self.valor1 = valor1
        self.valor2 = valor2
        self.valor3 = valor3
        
    def multiplicar(self):
        multiplicando = self.valor1 * self.valor2 * self.valor3
        return multiplicando
    
    def somar(self):
        somando = self.valor1 + self.valor2 + self.valor3
        return somando
    
os.system('cls')
valor1 = int(input('Digite o 1º valor: '))
valor2 = int(input('Digite o 2º valor: '))
valor3 = int(input('Digite o 3º valor: '))

calcular = Calcular(valor1, valor2, valor3)

resultado_soma = calcular.somar()
resultado_multiplicacao = calcular.multiplicar()

print(f'A multplicacao dos tres valores é: {resultado_multiplicacao}')
print(f'A soma dos tres valores é: {resultado_soma}')

    
