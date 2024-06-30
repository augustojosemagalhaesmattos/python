# Faça um programa para criar um dicionário com 5
# cores. Depois,  imprima as chaves e os valores deste dicionário.
import os


os.system('cls')

meu_dicionario = {'vermelho': 10, 'azul': 20, 'verde': 30, 'preto': 40, 'branco': 50 }

for cor, valor in meu_dicionario.items():
    print(f'Cor: {cor}, valor: {valor}')