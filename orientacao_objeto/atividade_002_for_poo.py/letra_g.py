# Faça um programa que calcule os números primos em um
# intervalo pré-determinado pelo usuário.

import os


class Primos:
    def __init__(self, inicio, fim):
        self.inicio = inicio
        self.fim = fim

    def e_primo(self, num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def calcular_primos(self):
        return [num for num in range(self.inicio, self.fim + 1) if self.e_primo(num)]


# Entrada de dados pelo usuário
os.system('cls')
inicio = int(input("Digite o início do intervalo: "))
fim = int(input("Digite o fim do intervalo: "))

if inicio > fim:
    print("O início do intervalo não pode ser maior que o fim.")
else:
    primos = Primos(inicio, fim).calcular_primos()
    print(f"Números primos entre {inicio} e {fim}: {primos}")

