# Faça um programa para criar um dicionário com 4 elementos.
import os


os.system('cls')

dicionario = {}

for i in range(1, 5):
    aluno = input(f'Digite o {i}º aluno: ').capitalize()
    carteira = input(f'Digite o numero da carteira do aluno: ')
    print('-'*50)
    dicionario[aluno] = carteira
    
 
print(dicionario)
print('-='*70)
print('---Digite mais 2 nomes---')
for i in range(1, 3):
    aluno = input(f'Digite o {i}º nome: ')
    carteira = input(f'Numero da carteira: ')
    print('-='*35)
    dicionario[aluno] = carteira

print(f'Lista atualizada: {dicionario}')