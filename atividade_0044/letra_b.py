# Faça um programa que receba o nome 'João da Silva'
# e, em seguida, substitua 'Silva' por 'Oliveira'.

import os


os.system('cls')

nome = 'João da Silva'

novo_nome = nome.replace("da Silva", "de Oliveira")

print(f"{novo_nome}")

