# Faça um programa com entrada de dados para calcular
# o perímetro de um retângulo.

import os


class Calcular:
    def __init__ (self, base, altura):
        self.base = base
        self.altura = altura
    
    def retangulo(self):
        perimetro = 2 * (base + altura)
        return perimetro
    
os.system('cls')
base = int(input('Digite o valor da base: '))
altura = int(input('Digite o valor da altura: '))

calcular = Calcular(base, altura)
ressultado = calcular.retangulo()

print('-'*70)
print(f'O perimetro do retangulo é: {ressultado}')



