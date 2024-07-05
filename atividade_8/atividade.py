# Trabalho sobre a estrutura de dados SET
# Senac Minas Gerais/Juiz de Fora
# Aluno: Augusto José Magalhães Mattos
# Turma: 0152
# Ano: 2024

import os


os.system('cls')

print('-='*35)
print("Bem-vindo ao gerenciador de convidados!")
print('-='*35)

convidados = set()

while True:
# Estou pedindo para o usuario para ele digitar o nome do convidado. Caso ele queira sair,
# vai digitar a palavra 'fim'
    nome = input("Digite o nome do convidado (ou 'fim' para sair): ").strip()

    if nome.lower() == 'fim':
        break  # Sai do loop se o usuário digitar 'fim'
    
    if nome:  # Verifica se o nome não está vazio
        convidados.add(nome) # Se o usuário inserir um nome válido (ou seja, não vazio), ele é adicionado ao conjunto convidados usando convidados.add(nome).
        print(f"Convidado '{nome}' adicionado!")

print("\nLista final de convidados:") 
for index, convidado in enumerate(convidados, start=1):
    print(f"{index}. {convidado}")

# Após o loop, uma lista final de convidados é impressa usando um loop for, enumerando cada convidado na ordem em que foram adicionados.

   


   
