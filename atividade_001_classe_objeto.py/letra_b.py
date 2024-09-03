# Faça um programa que peça o ano do seu nascimento e calcule
# a sua idade.
import os
from datetime import date


class Idade:
    def __init__(self, ano_atual, data_nascimento):
        self.ano_atual = ano_atual
        self.data_nascimento = data_nascimento
        
    def calculando_idade(self):
      data_atual = date.today()
      return self.ano_atual - self.data_nascimento
      

    







data_atual = date.today()