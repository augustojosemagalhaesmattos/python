# import
import os
import datetime


# limpando o terminal
os.system('cls')

print('-'*70)
print('Exercicio Letra B')
print('-'*70)

# Entrada com Casting
nascimento = int(input('Entre com seu nascimento: '))

# Processamento
ano_atual = datetime.datetime.now().year
idade = ano_atual - nascimento

# Saida interpolada
print(f'Sua idade é: {idade}')
