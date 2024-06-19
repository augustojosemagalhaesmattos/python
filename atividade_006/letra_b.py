# Crie uma lista com 5 números inteiros. Depois imprima a soma desses valores.

import os


os.system('cls')

print('-'*70)
print('Exercicio Letra B')
print('-'*70)

soma = 0

lista = 10, 20, 30, 40, 50

for indice, numero in enumerate(lista):
   print(f'{indice}: {numero}')
   soma += numero

print(f'A soma dos numeros é: {soma}')
print(f'{indice}: {lista}')
