import os


os.system('cls')

def separar_pares_impares(lista_numeros):
    numeros_pares = []
    numeros_impares = []
    
    for numero in lista_numeros:
        if numero % 2 == 0 :
            numeros_pares.append(numero)
        else:
            numeros_impares.append(numero)
            
    quantidade_pares = len(numeros_pares)
    quantidade_impares = len(numeros_impares)
    
    return numeros_pares, numeros_impares, quantidade_pares, quantidade_impares

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
pares, impares, quantidade_pares, quantidade_impares = separar_pares_impares(numeros)

print("Números pares:", pares)
print("Números ímpares:", impares)
print("Quantidade de números pares:", quantidade_pares)
print("Quantidade de números ímpares:", quantidade_impares)

