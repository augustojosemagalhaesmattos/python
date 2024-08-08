# Faça um programa que leia uma frase e depois exiba na tela:
# • A frase em minúsculas, a frase em maiúsculas, a quantidade de caracteres na frase e quantas letras tem a 2ª palavra na frase.
import os


os.system('cls') 

frase = 'Viva a estetica'

print('-'*70)
print('FRASE ORIGINAL: Viva a Estetica')
print('-'*70)

minuscula = frase.lower()
print(f'{minuscula}')

maiuscula = frase.upper()
print(f'{maiuscula}')

qts_caracteres = len(frase)
print(f'Essa frase tem {qts_caracteres} caracteres!')

palavras = frase.split()

print(f'Quantidade de letras na segunda palavra:', len(palavras[2]))