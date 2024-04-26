# Curso de Desenvolvimento de Sistemas
# Turma: 0152 (Braba)
# Autor: Augusto Mattos
# Data: 25/04/2024
# Estudo de Condicionais: Parte 3
# Operadores relacionais

import os


os.system('cls')

# Declaração
a = 10
b = 5
c = 'John'

print('-'*70)
print('Condicionais: Operadores lógicos')
print('-'*70)

# E (and) VERDADEIRO
print('E (and) VERDADEIRO')
if (a > 5 and b != c):
    print('Verdadeiro: Bloco executado')
else:
    print('Falso: Bloco executado')
    
print('.'*70)

# E (and) FALSO
print('E(and) FALSO')
if (a > 5 and b == c):
    print('Verdadeiro: Bloco executado')
else:
    print('Falso: Bloco executado')
    
print('.'*70)

# OU (or) VERDADEIRO
print('OU (or) VERDADEIRO')
if (a > 5 or b == c):
    print('Verdadeiro: Bloco executado')
else:
    print('Falso: Bloco executado')
    
print('.'*70)

# OU (or) FALSO
print('OU (or) FALSO')
if (a < 5 or c == 'jane'):
    print('Verdadeiro: Bloco executado')
else:
    print('Falso: Bloco executado')
print('-'*70)
print()