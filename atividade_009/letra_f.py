# Faça um programa que cadastra
# 5 tipos de vinho. Para os campos
# deste cadastro tome como referência 
# nome do vinho, tipo, teor alcoólico e safra.
import os


os.system('cls')

# Criação do dicionário para armazenar os vinhos
vinhos = {}

# Cadastro de 5 vinhos
vinhos["Vinho A"] = {
    "tipo": "Tinto",
    "teor_alcoolico": 12.5,
    "safra": 2018
}
vinhos["Vinho B"] = {
    "tipo": "Branco",
    "teor_alcoolico": 13.0,
    "safra": 2019
}
vinhos["Vinho C"] = {
    "tipo": "Rosé",
    "teor_alcoolico": 11.0,
    "safra": 2020
}
vinhos["Vinho D"] = {
    "tipo": "Espumante",
    "teor_alcoolico": 12.0,
    "safra": 2021
}
vinhos["Vinho E"] = {
    "tipo": "Sobremesa",
    "teor_alcoolico": 14.0,
    "safra": 2017
}

# Impressão dos vinhos cadastrados
for nome, dados in vinhos.items():
    print(f"Nome: {nome}, Tipo: {dados['tipo']}, Teor Alcoólico: {dados['teor_alcoolico']}%, Safra: {dados['safra']}")
