# Import
import os


# Limpar o terminal
os.system('cls')

print('-'*70)
print('Calcular o perimetro do retângulo')
print('-'*70)

# Entrada de Dados
base = float(input('Digite a base do retângulo: '))
altura = float(input('Digite a altura do retângulo: '))

# Processamento
perimetro = 2 * (base + altura)

# Saida interpolada
print(f'O perimetro é: {perimetro}')
