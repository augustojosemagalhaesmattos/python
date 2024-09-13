# Crie um programa que pede que o usuário digite um nome ou uma
# frase, verifique se esse conteúdo digitado é um palíndromo ou
# não, exibindo em tela esse resultado.

import os


class Polidromo:
    def __init__(self, string):
        self.string = string
    
    def vice_versa(self, string):
        pass
    
class String1(Polidromo):
    def __init__(self, string):
        self.string = string
        
    def vice_versa(self):
        
        conferindo = self.string[::-1]
        
        if self.string == conferindo:
            print(f'{self.string} é um palindromo! ')
        else:
            print('Não é um palindromo!')
            
        
        
os.system('cls')
string = input('Digite uma palavra: ').lower()
polidromo = String1(string)
polidromo.vice_versa()
