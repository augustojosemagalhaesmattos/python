# Crie uma função que cadastre o nome de uma aluno,
# a matrícula e a data de nascimento. Depois imprima
# os resultados cadastrados utilizando uma estrutura de repetição for.

import os


os.system('cls')

def cadastrar_aluno():
    alunos = []  
    
    while True:
        nome = input("Digite o nome do aluno (ou 'sair' para encerrar): ")
        if nome.lower() == 'sair':
            break
        
        matricula = input("Digite a matrícula do aluno: ")
        data_nascimento = input("Digite a data de nascimento do aluno: ")
        
        aluno = {
            'nome': nome,
            'matricula': matricula,
            'data_nascimento': data_nascimento
        }
        
        alunos.append(aluno)  
        
    return alunos

def imprimir_alunos(alunos):
    print("\nAlunos cadastrados:")
    for aluno in alunos:
        print(f"Nome: {aluno['nome']}")
        print(f"Matrícula: {aluno['matricula']}")
        print(f"Data de Nascimento: {aluno['data_nascimento']}")
        print("-" * 20)  


alunos_cadastrados = cadastrar_aluno()
imprimir_alunos(alunos_cadastrados)
