# Faça um programa que receba o nome completo de
# uma pessoa e, em seguida, mostre o primeiro e o último nome.

import os


os.system('cls')

print('='*70)
print('Exercicio letra I')
print('='*70)

# Entrada de Dados
nome = input('Digite seu nome completo:')

# Processamento


if nome != '':
    primeiro_ultimo = nome.split()
    primeiro_nome = primeiro_ultimo[0]
    ultimo = primeiro_nome[-1]  
    print(f'Seu primeiro nome é: {primeiro_nome}')
    print(f'Seu ultimo nome é: {ultimo}')
else: 
    print(f'Digite um nome.')
   

