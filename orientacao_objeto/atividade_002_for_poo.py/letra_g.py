# Faça um programa que calcule os números primos em um
# intervalo pré-determinado pelo usuário.

import os


class Numeros_Primos:
    def __init__(self, inicial, final):
        self.inicial = inicial
        self.final = final

    def intervalo(self, inical, final):
        pass


class Primos(Numeros_Primos):
    def __init__(self, inicial, final):
        self.inicial = inicial
        self.final = final

    def intervalo(self):
     for i in range(0, 101):
        for numero in range(inicio, fim + 1):
          if numero > 1:  # somente verifica números maiores que 1
            primo_atual = True
            for i in range(2, int(numero ** 0.5) + 1):
                if numero % i == 0:
                    eh_primo_atual = False
                    break
            if primo_atual:
                print(numero, end=" ")
                
inicio = int(input('Digite o 1º numero: '))
fim = int(input('Digite o 2º numero: '))

print()
numeros_primos = Primos(inicio, fim)
numeros_primos.intervalo
