# Faça um programa que imprima os números primos entre 0 e 100.

import os


class Primos:
    def __init__(self, inicial, final):
        self.inicial = inicial
        self.final = final

    def imprimir_primos(self, inicial, final):
        pass


class Priminhos(Primos):
    def __init__(self, inicial, final):
        self.inicial = inicial
        self.final = final

    def imprimir_primos(self):

        for i in range(self.inicial, self.final):
            for c in range(self.inicial, i):
                if i % c == 0:
                    break
            else:
                print(i, end=' | ')

os.system('cls')
primo = Priminhos(2, 101)
primo.imprimir_primos()
