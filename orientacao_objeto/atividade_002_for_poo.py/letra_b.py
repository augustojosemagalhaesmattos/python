# Evolua o programa anterior para um código que pergunte ao
# usuário qual o intervalo que ele deseja ver  impresso.

import os


class Intervalo:
    def __init__(self, inicio, fim):
        self.inicio = inicio
        self.fim = fim


class imprimir(Intervalo):
    def calcular_intervalo(self):
        for i in range(self.inicio, self.fim):
            print(f'{i}', end=" | ")


os.system('cls')
inicio = int(input('Digite o inicio do intervalo: '))
fim = int(input('Digite o fim do intervalo: '))


intervalo = imprimir(inicio, fim + 1)
intervalo.calcular_intervalo()
