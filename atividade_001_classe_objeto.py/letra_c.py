# Faça um programa que peça 4 notas, após a entrada de
# dados calcular a média das notas digitadas.

import os

class Media:
    def __init__(self, nota1, nota2, nota3, nota4):
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
        self.nota4 = nota4
        
    def valores(self, nota1, nota2, nota3, nota4):
        media = (nota1 + nota2 + nota3 + nota4) / 4
        return media
    
os.system('cls')
nota1 = int(input('Nota1: '))
nota2 = int(input('Nota2: '))
nota3 = int(input('Nota3: '))
nota4 = int(input('Nota4: '))

notas = Media(nota1, nota2, nota3, nota4)
resultado_media = notas.valores(nota1, nota2, nota3, nota4)

print(f'Nota 1: {nota1} | Nota 2: {nota2} |'
      f'Nota 3: {nota3} | Nota 4: {nota4}')
print('-'*70)
print(f'Média correta: {resultado_media}  ')
print('-'* 70)
        
        
    
         
        

