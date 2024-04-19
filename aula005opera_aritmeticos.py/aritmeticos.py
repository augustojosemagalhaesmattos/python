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
dividendo = float(input('Entre com o dividendo: '))
divisor = float(input('Entre com o divisor: '))

print()
print('--- RAIZ')
print('-'*70)
radicando = float(input('Entre com o radicando:'))

# Processamento
soma = parcela_1 + parcela_2
diferenca = minuendo - subtraendo
produto = multiplicando * multiplicador
quociente = dividendo / divisor
raiz_quadrada = radicando ** (1/2)
raiz_cubica = radicando ** (1/3)

# Saida
print('='*70)
print('RESULTADO')
print('-'*70)
print(f' A soma de {parcela_1} + {parcela_2} é: {soma}')
print(f'A subtração de {minuendo} - {subtraendo} é: {diferenca}')
print(f'A multiplicação de {multiplicando} * {multiplicador} é {diferenca}')
print(f'A divisão de {dividendo} / {divisor} é: {quociente}')
print(f'A raiz quadrada de {radicando} é {raiz_quadrada} +
e a raiz cubica é {raiz_cubica} ')

# Seguindo os passos anteriores, desenvolva o restante
# Acrescente a raiz quadrada e a raiz cúbica.
