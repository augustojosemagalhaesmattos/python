import os


os.system('cls')

print('-'*70)
print('Exercicio Letra A')
print('='*70)

# Entrada de Casting
numero = int(input('Digite um número inteiro: '))

# Processamento
if numero % 2 == 0:
    print(f'O número {numero:.0f} é par')
else:
    print(f'O número {numero} é impar!')
    

