#import
import os


print('-'*70)
print('Exercicio Letra F')
print('-'*70)

# Limpando o terminal
os.system('cls')

# Entrada de Dados
parcela = int(input('Digite um número:'))

# Processamento
soma_1 = parcela + parcela
soma_2 = parcela + parcela + parcela

# Saida interpolada
print(f'O dobro de {parcela} é {soma_1}')
print(f'O triplo de {parcela} é {soma_2}')

