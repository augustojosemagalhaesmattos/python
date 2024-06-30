# Faça um programa para criar um dicionário
# com 5  ferramentas. Depois,  imprima os valores 
# e a quantidade de elementos do dicionário.

import os


os.system('cls')

meu_dicionario = {
    'martelo': 'Pregar e remover parafusos',
    'chave de fenda': 'Para apertar ou soltar parafusos',
    'alicate': 'Para segurar ou apertar objetos',
    'serrote': 'Para cortar materias',
    'furadeira': 'Para fazer furos em superficies'
}
print('-'*70)
print('Valores das ferramentas:')
print('-'*70)
for descricao in meu_dicionario.values():
    print(descricao)

print('-'*70)
quantidade = len(meu_dicionario)
print(f'Quantidade de elementos no dicionario: {quantidade} ')
print('-'*70)