# Curso de Desencolvimento de Sistemas
# Turma 0152 (Braba)
# Autor: Augusto Mattos
# Data: 25/04/2024
# Estudo de Condicionais: Parte 2
# Objetivo: Prática com condicionais simples e aninhadas

import os


os.system('cls')

# Declarações
a = 10
b = 5
resposta = ''

print('-'*70)
print('Estudo de Condicional (Simples)')
print('='*70)

# Condicionais
if a > b:
    resposta = f'{a} é maior que {b}'
else:
    resposta = f'{a} não é maior que {b}'
# Saida
print('-'*70)
print(resposta)

# Declarações
a = 5
a = 5

print('-'*70)
print('Estudo de Condicional (aninhada)')
print('='*70)

if a > b:
    resposta = f'{a} é maior que {b}'
elif a < b:
    resposta = f'{a} é menor que {b}'
else:
    resposta = f'O valores são iguais: {a} = {b}'
# Saida
print('-'*70)
print(resposta)
print('-'*70)
print()