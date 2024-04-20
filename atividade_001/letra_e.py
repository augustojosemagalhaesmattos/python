# import 
import os


# limpando o terminal 
os.system('cls')

print('-'*70)
print('Exercicio Letra E')
print('-'*70)

# Entrada de Dados
numero = int(input('Digite um número inteiro: '))

# Processamento
sucessor = numero + 1
antecessor = numero - 1

# Saida interpolada
print(f'O sucessor de {numero} é {sucessor}')
print(f'O antecessor de {numero} é {antecessor}')
