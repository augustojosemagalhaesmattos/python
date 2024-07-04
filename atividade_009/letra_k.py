# Faça um programa que peça continuamente
# o nome e a idade de uma pessoa.
# Caso o usuário digite a idade 999,
# o programa será finalizado e executará uma impressão
# com os nomes cadastrados.
# Inicializando o dicionário para armazenar os dados
import os


os.system('cls')

pessoas = {}

while True:
    nome = input("Digite o nome da pessoa: ").capitalize()
    idade = int(input("Digite a idade da pessoa: "))
    
    if idade == 999:
        break
  
    pessoas[nome] = idade

print('-='*35)
print("Nomes cadastrados:")
print('-='*35)
for nome in pessoas.keys():
    print(nome)

