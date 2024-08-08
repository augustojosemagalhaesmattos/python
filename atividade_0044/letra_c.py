# Faça um programa que leia o nome de uma pessoa e verifique se a palavra 'Oliveira' está presente neste nome, mostrando True ou False.

import os


os.system('cls')

nome = 'João'

print(f'Nome: {nome}')
if 'Oliveira' in nome:
    print(f'O nome tem "Oliveira"!')
else:
    print(f'O nome não tem "Oliveira" presente!')
    