import os


os.system('cls')

print('-'*70)
print('ESTRUTURA DE CONTROLE SOMATORIO')
print('='*70)

print()

soma = 0

for var_iteradora in range(0, 4):
    numero = int(input(f'Digite o {var_iteradora + 1}º número: '))
    
    # Cálcule
    soma += numero # mesma coisa: soma = soma + numero
    
print('-'*70)
print(f'A soma dos números é: {soma}')
print('-'*70)
print()