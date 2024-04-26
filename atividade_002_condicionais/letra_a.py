import os


os.system('cls')

print('-'*70)
print('Exercicio Letra A')
print('='*70)

# Entrada de Casting
numero = int(input('Digite um número inteiro: '))
resposta = ''

# Condicional
if numero % 2 == 0:
    resposta = f'O número {numero: .0f} é par'
else:
    resposta = f'O número {numero} é impar!'
    
# Saida 
print('='*70)
print(resposta)

