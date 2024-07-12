# Faça um programa para criar um dicionário com 5  cores. Depois,  imprima as chaves e os valores deste dicionário.

import os


os.system('cls')

def main():
    
    cores = {
        "vermelho": 10,
        "verde": 20,
        "azul": 30,
        "amarelo": 40,
        "roxo": 50
    }

    print("Chaves do dicionário:")
    for cor in cores.keys():
        print(cor)

    print("\nValores do dicionário:")
    for valor in cores.values():
        print(valor)

    print("\nChaves e valores do dicionário:")
    for cor, valor in cores.items():
        print(f"{cor}: {valor}")

if __name__ == "__main__":
    main()
