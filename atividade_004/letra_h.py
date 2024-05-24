import os


os.system('cls')

print('-'*70)
print('Exercicio Letra H')
print('-'*70)

# Entrada de Dados
nome = str(input('Digite seu nome: '))

# Processamento
contar_o = nome.count('o')
primeira_o = nome.find('o') + 1
ultimo_o = nome.rfind('o') + 1

# Saida interpolada

if nome == '':
    print(f'Digite um nome.')
elif contar_o > 0:
    print(f'A letra "o" aparece uma {contar_o} vezes ')
    print(f'Primeira posição: {primeira_o} ')
    print(f'Ultima posição: {ultimo_o}  ')
else:
    print(f'A letra "o" não foi encontrado.')
    
