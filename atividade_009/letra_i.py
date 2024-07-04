# Faça um programa para criar um dicionário com 4 elementos.
# Depois imprima a lista completa, delete o último elemento
# e mostre uma listagem nova.

import os


os.system('cls')

meu_dicionario = {
    'carro': 10 ,
    'moto': 20 ,
    'bicicleta': 30,
    'avião': 40
}

print('-='*35)
print("Dicionário completo:")
print('-='*35)
for chave, valor in meu_dicionario.items():
    print(f"{chave}: {valor}")

# Deletando o último elemento
ultima_chave = list(meu_dicionario.keys())[-1]
del meu_dicionario[ultima_chave]

print('-='*35)
print("Dicionário após deletar o último elemento:")
print('-='*35)
for chave, valor in meu_dicionario.items():
    print(f"{chave}: {valor}")
