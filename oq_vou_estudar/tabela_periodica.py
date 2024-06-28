import os


os.system('cls')


print('-'*70)
print('----- TABELA PERIODICA -----')
print('='*70)

# Inicialização do dicionario e da lista
elementos = {} # Dicionario
periodica = [] # Lista

while True:
    os.system('cls')
    
    # Cabeçalho do menu
    print('-'*70)
    print('MENU DE OPÇÕES:')
    print('='*70)
    print('1. Adicionar um elemento')
    print('2. Visualizar todos os elementos')
    print('3. Atualizar um elemento')
    print('4. Remover um elemento')
    print('5. Sair')
    print('-'*70)
    
    # Solicitação da escolha do usuario
    opcao = input("Escolha uma opção (1-5):")
    
    if opcao == '1':
        # Adicionar um elemento
        simbolo = str(input('Simbolo do elemento: '))
        nome = str(input('Nome do elemento: '))
        elementos['simbolo'] = simbolo
        elementos['nome'] = nome
        periodica.append(elementos.copy())    
        input("\nElemento adicionado. Pressione Enter para continuar...")
        
    elif opcao == '2':
        # Visualizar todos os elementos
        print("\nElementos na tabela periodica:")
        print('-'*70)
        for elemento in periodica:
            for chave, valor in elemento.items():
                print(f'{chave.capitaliza()}: {valor}')
            print('-'*70)
        input("\nPressione Enter para continuar...")
        
    elif opcao == '3':
        # Atulizar um elemento
        simbolo = str(input('Digite o simbolo do elemento para atualizar: '))
        # Inicializa a flag como False
        encontrado = False
        for elemento in periodica:
            if elemento['simbolo'] == simbolo:
                novo_simbolo = str(input(f'Digite o novo simbolo para'
                f'{simbolo} (ou deixe em branco para manter o atual): '))
                novo_nome = str(input(f'Digite o novo nome para'
                f' {simbolo} (ou deixe em branco para manter o atual): '))
                
                # Atualiza o simbolo e o nome se fornecidos
                if novo_simbolo:
                    elemento['simbolo'] = novo_simbolo
                if novo_nome:
                    elemento['nome'] = novo_nome
                # Define a flag como True quando o elemento é encotrado
                encontrado = True
                break
            
            if encontrado:
                input("\nElemento atualizado. Enter para continuar...")
            else: 
                input("\nElemento não encotrado. Enter para continuar...")
                
    elif opcao == '4':
        # Remoer um elemento
        simbolo = str(
            input('Digite o simbolo do elemento que deseja remover: '))
        encontrado = False # Inicializa a flag como False
        for elemento in periodica:
            if elemento['simbolo'] == simbolo:
                periodica.remove(elemento)
                # Define a flag como True quando o elemento é encontrado
                encontrado = True
                break
        if encontrado:
            input("\nElemento removido. Enter para continuar...")
        else:
            input("\nElemento não encontrado. Enter para continuar...")
            
    elif opcao == '5':
        print("Saindo do programa.")
        break
    
    else:
        input("Opção invalida. Enter para tentar novamente...")

                
                