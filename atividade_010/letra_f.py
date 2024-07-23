# Crie uma função que receba 2 listas: 
# - lista 1: nome, peso, idade
# - lista 2: John, 40, 1.8
#   Sua função deverá criar um dicionário contendo chave e
#   valor utilizando como base essas duas listas. Depois,
#   seu programa deverá imprimir esse dicionário utilizando uma estrutura de repetição for.

import os


os.system('cls')

def criar_dicionario(lista_chaves, lista_valores):
    meu_dicionario = dict(zip(lista_chaves, lista_valores))
    
    for chave, valor in meu_dicionario.items():
        print(f'{chave}: {valor}')
   
lista_1 = ["nome", "peso", "altura"]
lista_2 = ["John", 40, 1.8]

criar_dicionario(lista_1, lista_2)