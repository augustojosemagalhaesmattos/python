# Faça um programa que solicite separadamente
# o nome, o nome do meio e o sobrenome de uma
# pessoa. Em seguida, imprima o nome completo.

import os


os.system('cls')

print('-'*70)
print('Exercicio Letra A')
print('-'*70)

# Entrada de Dados
nome = str(input('Seu primeiro nome: '))
nome_do_meio = str(input('Seu nome do meio: '))
sobrenome = str(input('Seu sobrenome: '))

juncao = "-".join([nome, nome_do_meio, sobrenome])

print(f'Seu nome completo é: {juncao}')

 
 
 