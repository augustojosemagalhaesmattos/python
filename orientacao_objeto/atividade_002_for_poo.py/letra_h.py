# Faça um programa que imprima os valores no intervalo
# definidos pelo usuário.  Defina 3 números que deverão ser 
# ignorados, ou seja, que não serão impressos na tela.


import os


class Classe_Pai:
    def __init__ (self, intervalo_inicial, intervalo_final):
        self.intervalo_inicial = intervalo_inicial
        self.intervalo_final = intervalo_final
    
    def numeros_ignorados(self, intervalo_inicial, intervalo_final):
        pass
    
class Classe_filha(Classe_Pai):

    def numeros_ignorados(self):
        ignorar = [10, 13, 15]
        if self.intervalo_inicial >= self.intervalo_final:
            print('Numero invalido')
        else:
            print(f'Sequencia de numeros: {self.intervalo_inicial} ate {self.intervalo_final}. Numeros a ignorar: {ignorar} ')
            
            for numero in range(inicio, fim + 1):
                if numero not in ignorar:
                    print(numero, end= ' | ')
                   
      
        
        
os.system('cls')
inicio = int(input('Digite o intervalo inicial: '))
fim = int(input('Digite o intervao final: '))

classe_pai = Classe_filha(inicio, fim)
resultado = classe_pai.numeros_ignorados()
        