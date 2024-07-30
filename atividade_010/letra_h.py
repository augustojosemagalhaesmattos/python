# Uma Academia deseja fazer uma pesquisa entre seus clientes para descobrir
# a média de altura  e peso de seus clientes. Faça um programa que pergunte
# a cada um dos clientes da academia seu código, nome, altura e peso. Após
# esse cadastramento, seu programa deverá listar os dados dos clientes e a média.
# Para sair do programa o usuário deverá digitar o valor zero(0). O número de clientes é indefinido. Veja a saída no próximo slide.

# Função para calcular a média

# Função para calcular a média
def calcula_media(valores):
    if len(valores) == 0:
        return 0
    return sum(valores) / len(valores)

clientes = []

while True:
    codigo = int(input("Digite o seu codigo (ou 0 para sair): "))
    if codigo == 0:
        break
    
    nome = input("Digite seu nome: ")
    altura = float(input("Digite a sua altura(em metros): "))
    peso = float(input("Digite o seu peso (em kg): "))
    
    cliente = {
        "codigo": codigo,
        "nome": nome,
        "altura": altura,
        "peso": peso
    }
    
    clientes.append(cliente)

# Listar os dados dos clientes
print("\nDados dos clientes cadastrados:")
for cliente in clientes:
    print(f"Código: {cliente['codigo']}, Nome: {cliente['nome']}, Altura: {cliente['altura']} m, Peso: {cliente['peso']} kg")

# Calcular as médias
alturas = [cliente['altura'] for cliente in clientes]
pesos = [cliente['peso'] for cliente in clientes]

media_altura = calcula_media(alturas)
media_peso = calcula_media(pesos)

# Exibir as médias
print(f"\nMédia de altura dos clientes: {media_altura:.2f} m")
print(f"Média de peso dos clientes: {media_peso:.2f} kg")
