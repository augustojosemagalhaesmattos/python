import os


os.system('cls')

print('-'*70)
print('Exercicio Letra H')
print('-'*70)

numeros_a_ignorar = [7, 13, 21]

inicio = int(input("Digite o número inicial do intervalo: "))
fim = int(input("Digite o número final do intervalo: "))

if inicio >= fim:
    print("Intervalo inválido. Certifique-se de que o início seja menor que o fim.")
else:
    print(f"Números no intervalo de {inicio} a {fim}, ignorando {numeros_a_ignorar}:")
    
    for numero in range(inicio, fim + 1):
        if numero not in numeros_a_ignorar:
            print(numero)