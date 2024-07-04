# Faça um programa para criar um dicionário
# com nomes de frutas. Em seguida
# verifique se tem abacaxi nos valores.

import os


os.system('cls')

frutas = {
    'fruta1': 'maçã',
    'fruta2': 'banana',
    'fruta3': 'laranja',
    'fruta4': 'abacaxi'
}
if 'abacaxi' in frutas.values():
    print("Abacaxi está no dicionário de frutas.")
else:
    print("Abacaxi não está no dicionário de frutas.")
