# Faça um programa que receba um número inteiro e mostre na tela:
# A quantidade de unidades, a quantidade de dezenas,
# a quantidade de centenas e a quantidade de milhares.

import os


os.system('cls')

# Entrada de Dados
numero = int(input('Digite um número inteiro: '))

# Processamento
milhares, resto = divmod(numero, 1000)
centenas, resto = divmod(resto, 100)
dezenas, unidades = divmod(resto, 10)

# Saida interpolada
print(f'Quantidade de unidades:', unidades)
print(f'Quantidade de dezenas:', dezenas)
print(f'Quantidade de centenas:', centenas)
print(f'Quantidade de milhares:', milhares)