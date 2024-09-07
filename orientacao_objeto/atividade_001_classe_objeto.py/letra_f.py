# Faça um programa que receba um número qualquer
# e calcule o dobro e o 
# triplo desse número
import os


class Dobro_Triplo:
    def __init__ (self, numero):
        self.numero = numero
    
    def dobro(self):
        dobrar = self.numero * 2
        return dobrar
    
    def triplo(self):
        triplicar = self.numero * 3
        return triplicar
    
os.system('cls')
numero = int(input('Digite um numero: '))

dobro_triplo = Dobro_Triplo(numero)

dobro = dobro_triplo.dobro()
triplo = dobro_triplo.triplo()

print('-'*70)
print(f'O dobro de {numero} é: {dobro}')
print(f'O triplo de {numero} é: {triplo}')
print('-'*70)
    
    
        
    
        