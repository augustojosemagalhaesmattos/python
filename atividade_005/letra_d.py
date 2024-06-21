# Faça um programa que imprima os números pares entre 0 e 100.

import os

os.system('cls')

for var_iteradora in range(0, 101):
    if var_iteradora % 2 == 0:
     print(var_iteradora , end=' | ')
  

