# Crie um programa que realiza a contagem de 1 até 100,
# usando apenas de números ímpares, ao final do processo exiba
# na tela quantos números ímpares foram encontrados nesse intervalo,
# assim como a soma dos mesmos.

import os


class Impares:
    def __init__(self, inicio, fim):
        self.inicio = inicio
        self.fim = fim
        
    def contagem(self, inicio, fim):
        pass
    
    def soma(self, inicio, fim):
        pass
    
    def quantidade_impares(self, inicio, fim):
        pass
    
class Numeros_impares(Impares):
    def __init__(self, inicio, fim):
        self.inicio = inicio
        self.fim = fim
        
    def contagem(self):
        print('-='*30)
        print('Numeros Impares!')
        print('-='*30)
        for numero in range(0, 101):
            if numero % 2 != 0:
                print(numero, end= ' | ')
                
    def soma(self):
        print()
        print()
        print('Soma dos Impares!')
        print('-='*30)
        soma = 0
        for numero in range(0, 101):
            if numero % 2 != 0:
                soma += numero
        print(soma)
        
    def quantidade_impares(self):
        print('-='*30)
        print('Quantidade de Numeros Impares!')
        print('-='*30)
        qts_impares = 0
        for numero in range(0, 101):
            if numero % 2 != 0:
                qts_impares += 1
        print(qts_impares)
                
 
                
    
                
                

                
impares = Numeros_impares(0, 101)
impares.contagem()
impares.soma()
impares.quantidade_impares()


                
            
                
    

    

