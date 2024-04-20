#import 
import os


print('-'*70)
print('Exercicio Letra G')
print('-'*70)


# Limpando o terminal
os.system('cls')

# Entrada de Dados
metros = float(input('Digite o valor em metros: '))

# Processamento
centimetros = metros * 100
milimetros = metros * 1000

# Saida interpolada
print(f'{metros} metros equivalem a: {centimetros} centimetros')
print(f'{metros} metros equivalem a: {milimetros} milimetros')
