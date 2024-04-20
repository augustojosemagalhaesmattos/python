# Import
import os


# Limpar o terminal
os.system('cls')

print('-'*70)
print('Calcular o perimetro do retângulo')
print('-'*70)

# Entrada de Dados
comprimento = float(input('Digite o comprimento do retângulo: '))
largura = float(input('Digite a largura do retângulo: '))

# Processamento
perimetro = 2 * (comprimento + largura)

# Saida interpolada
print(f'O perimetro é: {perimetro}')
