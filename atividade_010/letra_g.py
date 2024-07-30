# Crie um programa que peça ao usuário 2 números maiores que 0 e menores que 11. Depois mostre um menu com as seguintes operações:
# 1. Soma: 2. Subtração : 3. Produto : 4. Divisão : 4. Divisão inteira : 6. Resto da divisão.
# O usuário deverá escolher um número maior ou  igual a 1 e menor ou igual a 6. Em seguida, você criará funções que
# retornem os resultados das operações, imprimindo os resultados na tela.

import os


os.system('cls')

print('-'*70)
print('Exercicio letra G')
print('-'*70)

def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def produto(a, b):
    return a * b

def divisao(a, b):
    return a / b

def divisao_inteira(a, b):
    return a // b

def resto_divisao(a, b):
    return a % b

def menu():
    print("\nEscolha uma operação:")
    print("1. Soma")
    print("2. Subtração")
    print("3. Produto")
    print("4. Divisão")
    print("5. Divisão inteira")
    print("6. Resto da divisão")

num1 = int(input("Digite o primeiro número (maior que 0 e menor que 11): "))
num2 = int(input("Digite o segundo número (maior que 0 e menor que 11): "))

menu()
escolha = int(input("Digite o número da operação desejada: "))

if escolha == 1:
    print(f"A soma é: {soma(num1, num2)}")
elif escolha == 2:
    print(f"A subtração é: {subtracao(num1, num2)}")
elif escolha == 3:
    print(f"O produto é: {produto(num1, num2)}")
elif escolha == 4:
    print(f"A divisão é: {divisao(num1, num2)}")
elif escolha == 5:
    print(f"A divisão inteira é: {divisao_inteira(num1, num2)}")
elif escolha == 6:
    print(f"O resto da divisão é: {resto_divisao(num1, num2)}")
else:
    print("Escolha inválida. Por favor, escolha um número entre 1 e 6.")
