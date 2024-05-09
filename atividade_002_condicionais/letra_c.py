import os


os.system('cls')

print('-'*70)
print('Exercicio Letra C')
print('-'*70)

# Entrada de Dados
velocidade = float(input('Digite a velocidade: '))

# Velocidade
if velocidade <= 60:
    print(f'{velocidade}km/h, velocidade ideal. ')
else:
    print(f'{velocidade}km/h, favor reduzir a velocidade. ')
    
