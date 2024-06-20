# Faça um programa que procure na lista numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15] e produza:
#• O intervalo de 1 até 9
#• O intervalo de 8 até 13
#• Os números pares
#• Os números ímpares
#• Os múltiplos de 2, 3 e 4
#• Lista reversa
#• O produto dos intervalos 5-6 por 11-12

import os


os.system('cls')

print('-'*70)
print('Exercicio Letra C')
print('-'*70)

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# Intervalo de 1 até 9

intervalo_1_9 = numeros[0:9]
print("Intervalo de 1 até 9:", intervalo_1_9)
print('-'*70)

# Intervalo de 8 até 13

intervalo_8_13 = numeros[7:13]
print("Intervalo de 8 até 13:", intervalo_8_13)
print('-'*70)

# Números pares

numeros_pares = [num for num in numeros if num % 2 == 0]
print("Números pares:", numeros_pares)
print('-'*70)

# Números ímpares

numeros_impares = [num for num in numeros if num % 2 != 0]
print("Números ímpares:", numeros_impares)
print('-'*70)

# Múltiplos de 2, 3 e 4

multiplos_2_3_4 = [num for num in numeros if num % 2 == 0 or num % 3 == 0 or num % 4 == 0]
print("Múltiplos de 2, 3 ou 4:", multiplos_2_3_4)
print('-'*70)

# Lista reversa

lista_reversa = numeros[::-1]
print("Lista reversa:", lista_reversa)
print('-'*70)

# Produto dos intervalos 5-6 por 11-12
produto_intervalos = numeros[4:6] + numeros[10:12]
produto = 1
for num in produto_intervalos:
    produto *= num
print("Produto dos intervalos 5-6 por 11-12:", produto)
print('-'*70)