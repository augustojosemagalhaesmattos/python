# import
import os

# limpar o terminal
os.system('cls')

print('-'*70)
print('Exercicio Letra D')
print('-'*70)

# Entrada com Casting
print('-'*70)
numero1 = float(input('Digite o primeiro número '))
numero2 = float(input('Digite o segundo número '))

# Processemnto
resultado_divisao = numero1 / numero2

# Saida interpolada
print('-'*70)
print('RESULTADO')
print(f'o resultado da divisão é: {resultado_divisao:.4f}')