# Faça um programa que some a quantidade de números pares
# encontrados no intervalo entre 0 e 100.

import os

os.system('cls')


class Numeros_Pares:
    def __init__(self, numero, final):
        self.numero = numero
        self.final = final

    def imprimir_numeros(self, numero, final):
        pass


class Numeros(Numeros_Pares):
    def __init__(self, numero, final):
        self.numero = numero
        self.final = final

    def imprimir_numeros(self):
        soma = 0
        for numero in range(self.numero, self.final):
            if numero % 2 == 0:
                soma += 1
        print(soma)


os.system('cls')
numeros_pares = Numeros(0, 101)
numeros_pares.imprimir_numeros()
