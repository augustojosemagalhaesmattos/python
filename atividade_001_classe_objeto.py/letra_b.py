# Faça um programa que peça o ano do seu nascimento e calcule
# a sua idade.
import os
from datetime import datetime


class Calculando:
    def __init__(self, data_nascimento):
        self.data_nascimento = data_nascimento
        
    def calculando_idade(self, data_nascimento):
      data_atual = datetime.now().year
      conta = data_atual - data_nascimento
      return conta
  
os.system('cls')
idade = int(input('Digite sua data de nascimento: '))
    
ano = Calculando(idade)

print('-'*70)
print(f'Você tem: {ano.calculando_idade(idade)}')









