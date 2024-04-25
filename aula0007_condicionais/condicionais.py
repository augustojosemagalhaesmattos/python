# Curso de Desenvolvimento de Sisemas
# Turma 0152 (Braba)
# Autor: Sebastião Marcos
# Data: 12/04/2024
# Estudo de Condicionais: Parte 1 
# Objetivo: Verificando um valor decimal

import os


os.system('cls')

print('-'*70)
print('Estudo de Condicional: Parte 1')
print('='*70)

# Entrada
valor = float(input('Digite um número: '))
resposta = ''

# Condicional
if valor % 2 == 0:
    resposta = f'Entrada incorreta< o valor {valor: .0f} é um inteiro!'
else:
    resposta = f'Entrada correta, valor {valor} é um decimal!'
    
    # Saida
print('='*70)
print(resposta)

print('Fim do programa!\n') # \n salta um linha