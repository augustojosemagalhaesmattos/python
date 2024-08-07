import os


os.system('cls')

# definindo uma função para empacotar
def empacotar(*lista_numeros):
    print(f'Empacotados: {lista_numeros}')
    for i in lista_numeros:
        print(f'Empacotado: {i}')
        
    # invocando a função empacotar
empacotar(1, 2, 3, 4, 5)
    
    # Desempacotar (Lista)
def desempacotar(a, b, c, d, e):
        print('Desempacotar:')
        print(f'a = {a}')
        print(f'b = {b}')
        print(f'c = {c}')
        print(f'd = {d}')
        print(f'e = {e}')
        
# Invocando a função empacotar
lista_numeros = [1, 2, 3, 4, 5,] # lista
desempacotar(*lista_numeros) # * args

# packing Dicionario
def empacotar_dicionario(**dados_dicionario): # **Kwargs
    print(f'Dados do dicionario: {dados_dicionario}')
    for k, v in dados_dicionario.items():
        print(f'Chave: {k}, valor: {v}')
        
print('-'*70)
print('---Dicionario')
empacotar_dicionario(nome = 'Juquinha', idade = 70, peso = 70.5)

# Unpacking Dicionario
print('-'*70)
def desempacotar_dicioanario(nome, idade, peso):
    print(f'Nome = {nome}')
    print(f'Idade = {idade}')
    print(f'Peso = {peso}')

dicionario = dict(nome = 'Maria', idade = 70, peso = 70.5)
desempacotar_dicioanario(**dicionario)
print()
    
    