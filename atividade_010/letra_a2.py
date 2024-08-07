# Crie uma função que receba uma lista de números.
# Depois retorne duas listas com os números pares,
# os números ímpares, a quantidade de números pares
# e a quantidade de números ímpares.

import os


os.system('cls')
numeros = [1, 2, 3, 4, 5, 6, 7, 8]

def separar_pares_impares(numeros):
    numeros_pares = []
    numeros_impares = []
    
    for numero in numeros:
        if numero % 2 == 0:
            numeros_pares.append(numero)
            qts_pares = len(numeros_pares)
            
        else:
            numeros_impares.append(numero)
            qts_impares = len(numeros_impares)
            
    
    print(f'Numeros pares: {numeros_pares}, quantidade de pares: {qts_pares} ', end=' ')
            
separar_pares_impares(numeros)
   

    





            
        
    
    