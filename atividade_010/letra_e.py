# Faça um programa para criar um dicionário com 5  ferramentas. Depois,
# imprima os valores e a quantidade de elementos do dicionário.

import os


os.system('cls')

def main():
    
    ferramenta = {
        "martelo": 10,
        "furadeira": 20,
        "chave de fenda": 30,
        "serrote": 40,
        "alicate": 50
    }

    

    print("\nValores do dicionário:")
    for valor in ferramenta.values():
        print(valor)

    quantidade = len(ferramenta)
    print(f'Quatidade de ferramentas: {quantidade}')
 
if __name__ == "__main__":
    main()