# Faça um programa para criar um dicionário com 4 elementos.
import os


os.system('cls')

dicionario = {}

for i in range(1, 5):
    aluno = input(f'Digite o {i}º aluno: ').capitalize()
    carteira = input(f'Digite o numero da carteira do aluno: ')
    print('-'*50)
    dicionario[aluno] = carteira
    
print('-='*30)    
print(dicionario)