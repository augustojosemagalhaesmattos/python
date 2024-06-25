import os


os.system('cls')

print('-'*70)
print('Atividade 8')
print('-'*70)

# Criando um conjunto vazio
conjunto = set()

# Pedindo ao usuário para inserir elementos
print("Liste as tarefas que você tem que fazer ou já fez: (Digite 'fim' para parar):")

while True:
    elemento = input("Elemento: ")

    if elemento.lower() == 'fim':
        break
    
    # Adicionando o elemento ao conjunto usando o método add()
    conjunto.add(elemento)

# Mostrando conjunto atual
print("Conjunto atual:", conjunto)
