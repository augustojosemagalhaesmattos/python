# Crie um programa que realiza a 
# contagem de 1 até 100, usando apenas
# de números ímpares, ao final do processo
# exiba na tela quantos números ímpares foram
# encontrados nesse intervalo, assim como a soma dos mesmos.


import os


os.system('cls')

soma = 0

for var_iteradora in range(1, 101):
    if var_iteradora % 2 == 0:
        print()
    else:
       print(f'Numeros impares: "{var_iteradora}" ', end= ' ')
        
    soma += var_iteradora
print(f'Soma é: {soma}')
        
        