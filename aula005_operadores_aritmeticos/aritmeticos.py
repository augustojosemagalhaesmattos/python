# imports
import os

#limpar o terminal
os.system('cls')

print('-'*70)
print('OPERADORES ARITMÉTICOS')
print('='*70)

# Entrada de Dados
print('--- SOMA')
print('-'*70)
parcela_1 = float(input('Entre com a 1ª parcela: '))
parcela_2 = float(input('Entre com a 2ª parcela: '))

print()
print('--- SUBTRAÇÂO')
print('-'*70)
minuendo = float(input('Entre com o minuendo: '))
subtraendo = float(input('Entre com a subtraendo: '))

print()
print('--- PRODUTO')
print('-'*70)
multiplicando = float(input('Entre com o multiplicando: '))
multiplicador = float(input('Entre com o multiplicando: '))

print()
print('--- DIVISAO')
print('-'*70)
dividendo = float(input('Entre com o dividendo '))
divisor = float(input('Entre com o divisor '))

# Processamento
soma = parcela_1 + parcela_2
diferenca = minunedo - subtraendo
produto = multiplicando * multiplicador
quociente = dividendo / divisor

# Saida
print('='*70)
print('RESULTADO')
print('-'*70)
print(f' A soma de {parcela_1} + {parcela_2} é: {soma}')
print(f'A subtração de {minuendo} - {subtraendo} é: {diferenca}')
print(f'A multiplicação de {multiplicando} * {multiplicador} é {diferenca}')
print(f'A divisão de {dividendo} / {divisor} é: {quociente}')

# Seguindo os passos anteriores, desenvolva o restante
# Acrescente a raiz quadrada e a raiz cúbica.