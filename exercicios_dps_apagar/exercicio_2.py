import os


os.system('cls')

numeros = [10, 20, 30 , 40, 50]
soma = 0

for numero in numeros:
    soma += numero

media = soma / len(numeros)
print(f'A media é: {media}')