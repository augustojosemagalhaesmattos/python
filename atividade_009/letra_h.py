# Faça um programa para ler o dicionário
# nomes = {‘nome’: ’John, ‘idade’: 40, ‘peso’: 80, ‘altura’: 1.70}. Em
# seguida realize as seguintes ações:

# - Listar chaves e valores com laço - Deletar o peso
# - Listar novamente chaves e valores - mostrar o nome e altura
import os

os.system('cls')

meu_dicionario = {'nome': 'john', 'idade': 40, 'peso': 80, 'altura': 1.70}

print('-='*35)
print("Chaves e valores antes de deletar 'peso': ")
for chave, valor in meu_dicionario.items():
    print(f"{chave}: {valor}")
print('-='*35)
    
del meu_dicionario ['peso']

print("Chaves e valores apos deletar 'peso': ")
for chave, valor in meu_dicionario.items():
    print(f"{chave}: {valor}")
print('-='*35)

print('Nome e altura:')
print()
print(f"Nome: {meu_dicionario['nome']}")
print(f"Altura: {meu_dicionario['altura']}")    




