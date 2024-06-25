# ff
import os


os.system('cls')

# Solicitar ao úsuario a quantidade de elementos na tupla
numero_elementos = int(input("Quantos elementos na tupla? "))

# inicializar uma lista vazia para armazenar os elementos
elementos = []

# Estrutura de repetição para obter os elemnetos do úsuario
for i in range(numero_elementos):
    while True:
        valor = input(f"Digite o valor  {i + 1}: ")
        if valor.isdigit(): # Verifica s a entrada é um elemento
            elementos.append(int(valor))
            break
        else:
            print("Entrada inválid. Digite um número.")
            
# Converter a lista para uma tupla
tupla = tuple(elementos)

print('-'*70)
# Exibir a tupla criada
print(f"Tupla criada: {tupla}")
print('-'*70)

# Estrutura de repettição para permitir múltiplas
# operações até que o úsuario deseje sair
while True:
    # Condicional para verificar a presença de 
    # um numero especifico
    valor = int(input("Verificar se o número na Tupla: "))
    
    if valor in tupla:
        print(f"O número {valor} está na tupla.")
        # Contar quantas vezes o número aparece
        
        
        contagem = tupla.count(valor)
        print(f"O número {valor} aparece {contagem} vez(es).")
        # Encontrar o indice da primeira ocorrencia
        
        indice = tupla.index(valor)
        print(f"A 1ª ocorrencia de {valor} está no indice {indice}.")
        
    else:
        print(f"O número {valor} não está na tupla.")
        
    # Perguntar ao usuário se deseja realizar
    # outra operação ou sair
    continuar = input("Deseja Continuar? (s/n): "). lower()
    if continuar != 's':
      print("Encerrando o programa. Até mais!") 
    break

print('-'*70)
print('Fim do programa!')
print('-'*70)       
