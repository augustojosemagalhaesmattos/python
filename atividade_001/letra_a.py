# import
import os


os.system('cls')

print('-'*70)
print('Exercicio Letra A')
print('-'*70)

# Entrada
nota1 = float(input('1ª nota: '))
nota2 = float(input('2ª nota: '))
nota3 = float(input('3ª nota: '))

# Processamento
soma = nota1 + nota2 + nota3
multiplicacao = nota1 * nota2 * nota3

# Saida interpolada
print('-'*70)
print(f'a soma das notas: {soma}')
print(f'a multiplicacao das notas: {multiplicacao}')