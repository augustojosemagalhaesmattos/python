# Crie uma função que receba uma lista de números.
# Depois retorne duas listas com os números pares,
# os números ímpares, a quantidade de números pares
# e a quantidade de números ímpares.

import os


os.system('cls')


def separar_impar_par(lista_numero):
    
   numeros_pares = []
   numeros_impares = []

   for numero in lista_numero:
        if numero % 2 == 0:
           numeros_pares.append(numero)
        else:
           numeros_impares.append(numero)
           
   quantidade_pares = len(numeros_pares)
   quantidade_impares = len(numeros_impares)
    
   return numeros_pares, numeros_impares, quantidade_pares, quantidade_impares

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
nuemros_pares, numeros_impares, quantidade_pares, quantidade_impares = separar_impar_par(numeros)

print(f'Numeros pares: {nuemros_pares}')
print(f'Numeros impares: {numeros_impares}')
print(f'Quantidade de numeros pares: {quantidade_pares}')
print(f'Quantidade de numeros impares: {quantidade_impares}')