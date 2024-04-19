#import
import os

os.system('cls')

print('-'*70)
print('Exercicio Letra C')
print('-'*70)

# Entrada com Casting
nota1 = float(input('1ª nota: '))
nota2 = float(input('2ª nota: '))
nota3 = float(input('3ª nota: '))
nota4 = float(input('4ª nota: '))

# Processamento
soma = nota1 + nota2 + nota3 + nota4
media = (nota1 + nota2 + nota3 + nota4) / 4

# Saida interpolada
print('-'*70)
print(f'Nota 1: {nota1} | Nota 2: {nota2} |'
      f'Nota 3: {nota3} | Nota 4: {nota4}')
print('-'*70)
print(f'Média correta: {media} ')
print('-'* 70)
