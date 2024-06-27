# Trabalho sobre a estrutura de dados SET
# Senac Minas Gerais/Juiz de Fora
# Aluno: Augusto José Magalhães Mattos
# Turma: 0152
# Ano: 2024

import os


os.system('cls')

print('='*70)
print('Lista de tarefas')
print('='*70)

# Criando um conjunto vazio
conjunto = set()

# Pedindo ao usuário para inserir elementos
print('-'*70)
print("Liste suas tarefas ")
print('-'*70)

while True:
    elemento = input("Elemento: ")

    if elemento.lower() == 'fim':
        break
    
    # Adicionando o elemento ao conjunto usando o método add()
    conjunto.add(elemento)

# Mostrando conjunto atual
print("Conjunto atual:", conjunto)
