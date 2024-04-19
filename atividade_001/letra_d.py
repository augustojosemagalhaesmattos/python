# import
import os

# limpar o terminal
os.system('cls')

print('-'*70)
print('Exercicio Letra D')
print('-'*70)

# Entrada com Casting
print()
print('--- DIVISAO')
print('-'*70)
dividendo = float(input('Entre com o dividendo: '))
divisor = float(input('Entre com o divisor: '))

# Processemnto
quociente = dividendo / divisor

# Saida interpolada
print('-'*70)
print('RESULTADOS')
print('-'*70)
print(f'A divisão de {dividendo} / {divisor} é: {quociente}')