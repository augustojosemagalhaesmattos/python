import os


os.system('cls')

print('-'*70)
print('Exercicio Letra F')
print('-'*70)

# Entrada de Dados
ano = int(input('Por favor, insira um ano:'))

# Processo
if ano % 100 != 0 and ano % 4 == 0:
    print(f'{ano} é um ano bissexto')
else: 
    print(f'{ano} não é um ano bissexto')


