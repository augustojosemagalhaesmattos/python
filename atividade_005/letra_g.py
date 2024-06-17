import os


os.system('cls')

print('-'*70)
print('Exercicio Letra G')
print('-'*70)

inicio = int(input("Digite o número inicial do intervalo: "))
fim = int(input("Digite o número final do intervalo: "))

# Validação dos limites
if inicio >= fim or inicio < 0:
    print("Intervalo inválido. Certifique-se de que o início seja menor que o fim.")
else:
    print(f"Números primos no intervalo de {inicio} a {fim}:")
    
    # Iteração sobre o intervalo e verificação de primos
    for numero in range(inicio, fim + 1):
        if numero > 1:  # somente verifica números maiores que 1
            primo_atual = True
            for i in range(2, int(numero ** 0.5) + 1):
                if numero % i == 0:
                    eh_primo_atual = False
                    break
            if primo_atual:
                print(numero, end=" ")