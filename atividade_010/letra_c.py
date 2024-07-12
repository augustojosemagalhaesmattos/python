# Crie uma função que verifica se uma aluno 
# está cadastrado ou não em um dicionário.
# Se estiver cadastrado, imprima o nome desse
# aluno e o resto dos seus dados. O dicionário 
# deverá conter nome, matrícula e a data de nascimento do aluno.

import os


os.system('cls')

def verificar_aluno(cadastro_alunos, nome_aluno):
    if nome_aluno in cadastro_alunos:
        aluno = cadastro_alunos[nome_aluno]
        print(f"Nome: {aluno['nome']}")
        print(f"Matrícula: {aluno['matricula']}")
        print(f"Data de Nascimento: {aluno['data_nascimento']}")
    else:
        print(f"Aluno '{nome_aluno}' não encontrado no cadastro.")


cadastro_alunos = {
    "João": {
        "nome": "João da Silva",
        "matricula": "123456",
        "data_nascimento": "01/01/2000"
    },
    "Maria": {
        "nome": "Maria Souza",
        "matricula": "654321",
        "data_nascimento": "15/05/1999"
    }
}

nome_aluno = input("Digite o nome do aluno que deseja verificar: ").capitalize()

verificar_aluno(cadastro_alunos, nome_aluno)

