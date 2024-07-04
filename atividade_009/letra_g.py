import os
import random


os.system('cls') 

meu_dicionario = {}

print('-='*35)
print('Cadastre 4 alunos')
print('-='*35)

for i in range(1, 5):      
    nome = input(f'Nome do {i}º aluno: ').capitalize()
    data = input(f'Data de nascimento do aluno:')
    numero_aleatorio = random.randint(1001, 9999)
    meu_dicionario[nome] = {"data": data, "matricula": numero_aleatorio}
    print(f'Número da matrícula: {numero_aleatorio}')
    print() 
    print('-='*35)

print('Dados dos Alunos:')
print('-='*35)
for nome, dados in meu_dicionario.items():
    print(f"Nome: {nome}, Data de Nascimento: {dados["data"]}, Número da Matrícula: {dados["matricula"]} ")
    print('-='*35)
