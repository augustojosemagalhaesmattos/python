import os


os.system

print('-'*70)
print('Exercicio Letra B')
print('-'*70)

# Entrada de Dados
numero1 = float(input('Digite o primeiro número: '))
numero2 = float(input('Digite o segundo número: '))
numero3 = float(input('Digite o terceiro numero: '))

# Maior
if (numero1 > numero2 > numero3):
    print (f'{numero1: .0f} é o maior numero')
    
    
elif (numero2 > numero1 > numero3):
    print (f'{numero2: .0f} é o maior numero')
    
else:
    print (f'{numero3: .0f} é o maior numero')
    
# Menor
if (numero1 < numero2 < numero3):
    print (f'{numero1: .0f} é o menor numero')
    
    
elif (numero2 < numero1 < numero3):
    print (f'{numero2: .0f} é o menor numero')
    
else:
    print (f'{numero3: .0f} é o menor numero')
    
# Igual
if (numero1 == numero2 == numero3):
    print (f'{numero1: .0f} é igual')
    
else:
    print (f'os numeros não são iguais')
    

    
# Saida
print('-'*70)