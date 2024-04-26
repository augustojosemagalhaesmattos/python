# Curso de Desenvolvimento de Sisemas
# Turma 0152 (Braba)
# Autor: Augusto Mattos
# Data: 12/04/2024
# Estudo de Condicionais: Parte 1 
# Objetivo: Verificando um valor decimal

import os


os.system('cls')

print('-'*70)
print('Estudo de Condicional: Parte 1')
print('='*70)

# Entrada
numero = float(input('Digite um número: '))
resposta = ''

# Condicional
if numero % 2 == 0:
    resposta = f'O número {numero: .0f} é par'
else:
    resposta = f'O número {numero} é impar!'
    
    # Saida
print('='*70)
print(resposta)

print('Fim do programa!\n') # \n salta um linha