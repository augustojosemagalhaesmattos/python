# Faça um programa que some a quantidade de números pares encontrados no intervalo entre 0 e 100.

import os


os.system('cls')

soma = 0

for var_iteradora in range(0, 101):
    if var_iteradora % 2 == 0:
     print(var_iteradora , end=' | ')
    soma += var_iteradora

print(f'\nA soma é: {soma}')

    