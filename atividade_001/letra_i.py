# import
import os 


# Limpando o Terminal
os.system('cls')

print('-'*70)
print('Exercicio Letra I')
print('-'*70)

# Entrada de Saida
numero = int(input('Digite um valor em Reais:'))

# Processaemnto
multiplicacao = numero * 5

# Saida interpolada
print(f'{numero} real convertendo em dólares é {multiplicacao} dólares')
