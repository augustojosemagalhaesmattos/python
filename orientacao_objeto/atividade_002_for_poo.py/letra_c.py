# Faça um programa que imprima os números
# no intervalo entre 1 e 10 em ordem inversa.
import os


class Intervalo:
    def __init__(self, inicio, fim):
        self.inicio = inicio
        self.fim = fim
        
class imprimir(Intervalo):
    def calcular_intervalo(self):
     for i in range(fim, inicio - 1, -1):
         print(i, end= ' | ')
          
os.system('cls')
fim = int(input('Digite o fim do intervalo: '))
inicio= int(input('Digite o inicio do intervalo: '))


intervalo = imprimir(fim, inicio)
intervalo.calcular_intervalo()
