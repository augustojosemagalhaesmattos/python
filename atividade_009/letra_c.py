# Utilizando o exercício anterior , retire um elemento do dicionário.
import os


os.system('cls')

dicionario = {}
print('Adicione 4 alunos')
print('-='*30)
for i in range(1, 5):
    aluno = input(f'Digite o {i}º aluno: ').capitalize()
    carteira = input(f'Digite o numero da carteira do aluno: ')
    print('-'*50)
    dicionario[aluno] = carteira
    
print('-='*40)    
print(dicionario)
print('-='*40)
print()
print('---Digite mais dois alunos---')
print()

for i in range(1, 3):

    aluno = input(f'Digite o {i}º aluno ').capitalize()
    carteira = input(f'Digite o numero da carteira: ')
    dicionario[aluno] = carteira
    print('-'*30)
    
print('-='*40)
print(dicionario)

aluno = input(f'Nome do aluno que deseja remover: ').capitalize()
remover_aluno = dicionario.pop(aluno)

print(f'aluno: {aluno}: {remover_aluno} removido com sucesso!')