import random
import os

os.system('cls')

print('-'*70)
print('Exercicio letra I')
print('-'*70)

def pergunta_capital(estados_capitais):
    estado, capital = random.choice(list(estados_capitais.items()))
    resposta = input(f"Qual é a capital do estado {estado}? ")
    return resposta.strip().lower() == capital.lower()

# Dicionário com estados e suas capitais
estados_capitais = {
    "Acre": "Rio Branco",
    "Alagoas": "Maceió",
    "Amapá": "Macapá",
    "Amazonas": "Manaus",
    "Bahia": "Salvador",
    "Ceará": "Fortaleza",
    "Distrito Federal": "Brasília",
    "Espírito Santo": "Vitória",
    "Goiás": "Goiânia",
    "Maranhão": "São Luís",
    "Mato Grosso": "Cuiabá",
    "Mato Grosso do Sul": "Campo Grande",
    "Minas Gerais": "Belo Horizonte",
    "Pará": "Belém",
    "Paraíba": "João Pessoa",
    "Paraná": "Curitiba",
    "Pernambuco": "Recife",
    "Piauí": "Teresina",
    "Rio de Janeiro": "Rio de Janeiro",
    "Rio Grande do Norte": "Natal",
    "Rio Grande do Sul": "Porto Alegre",
    "Rondônia": "Porto Velho",
    "Roraima": "Boa Vista",
    "Santa Catarina": "Florianópolis",
    "São Paulo": "São Paulo",
    "Sergipe": "Aracaju",
    "Tocantins": "Palmas"
}

corretas = 0

while True:
    if pergunta_capital(estados_capitais):
        corretas += 1
        print("Correto!")
    else:
        print("Resposta errada!")
        break

print(f"\nVocê acertou {corretas} perguntas.")
