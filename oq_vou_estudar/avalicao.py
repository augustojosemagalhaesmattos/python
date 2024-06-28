import os


os.system('cls')

# Inicialização do dicionario e da lista
elementos = {} # Dicionario
periodica = [] # Lista

# Entrada de Dados
for c in range(2): # Considerando a entrada de 2 elementos
    print(f"Entrada de dados {c + 1}:")
    simbolo = str(input('Simbolo do elemento: '))
    nome = str(input('Nome do elemento: '))
    
    # Adiciona os dados ao dicionario
    elementos['simbolo'] = simbolo
    elementos['nome'] = nome
    
    # Usa append() com copy() para adicionar um copia do dicionario a lista
    periodica.append(elementos.copy())
    
print()
print('-'*70)
print("Elementos na tabela periodica:")
print(periodica)
print('-'*70)
print()

# For aninhando para percorrer a lista e o dicionario
print("Detalhes dos elementos:")
for elemento in periodica: # Para cada elemento na lista
    for chave, valor in elemento.items(): # Para cada chave e valor do dicionario
        print(f'{chave.capitalize()}: {valor}') # Imprime a chave e o valor de maneira legivel
    print('-'*70) # Linha separadora entre elementos
    
        
        
