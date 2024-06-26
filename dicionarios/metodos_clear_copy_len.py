import os


os.system('cls')
# Criação do dicionario vazio
meu_dicionario = {}

while True:
    print('-'*70)
    # Exibição do menu de opções
    print("\nMenu de opções:")
    print("1. Adicionar um par chave-valor")
    print("2. Mostrar o dicionario")
    print("3 Mostrar o tamnho do dicionario")
    print("4. Fazer uma copia do dicionario")
    print("6. Sair")
    print('-'*70)
    
    # Solicitação da escolha do usuario
    opcao = input("Escolha uma opção (1-6): ")
    
    if opcao == '1':
        # Adiciona um novo par chave-valor ao dicionario
        chave = input("Digite a chave: ")
        valor = input("Digite o valor: ")
        meu_dicionario[chave] = valor
        print(f"Par {chave}: {valor} adicionado.")
        
    elif opcao == '2':
        # Exibe o dicionario atual
        print("Dicionário atual:", meu_dicionario)
        
    elif opcao == '3':
        # Mostra o tamanho do dicionario usando len()
        tamanho = len(meu_dicionario)
        print(f"O dicionario tem {tamanho} elementos.")
        
    elif opcao == '4':
        # Cria uma cópia do dicionario usando copy() e exibe a copia
        copia_dicionario = meu_dicionario.copy()
        print("Cópia do dicionario:", copia_dicionario)
        
    elif opcao == '5':
        #limpar o dicionario usando clear()
        meu_dicionario.clear()
        print("Dicionario limpo.")
        
    elif opcao == '6':
        # Sai do programa
        print("saindo do programa.")
        break
        
    else:
        # Mensagem para opção invalida
        print("Opção invalida. Tente novamente.")