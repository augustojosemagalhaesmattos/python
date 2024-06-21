# Faça um programa que imprima os números no intervalo entre 1 e 100.
# Os números devem ser apresentados na horizontal.

import os 


os.system('cls')

print('-'*70)
print('Exercicio Letra A')
print('-'*70)


for var_iteradora in range(1, 101):
   print(f'{var_iteradora}', end=" | ")