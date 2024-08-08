# Faça um programa que solicite separadamente o nome,
# o nome do meio e o sobrenome de uma pessoa. Em seguida,
# imprima o nome completo.

import os


os.system('cls')

nome = input('Digite seu primeiro nome: ')
nome_meio = input('Digite seu nome do meio? ')
sobrenome = input('Digite seu sobrenome: ')

juncao = "-".join([nome  + nome_meio + sobrenome])

print(f'Seu nome completo é: {juncao}')
