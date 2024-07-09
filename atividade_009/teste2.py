import os


os.system('cls')

meu_dicionario = {}

while True:
    print('-='*35)
    print('1. Nome do contato e numero de telefone: ')
    print('2. Contato que deseja remover: ')
    print('3. Ver Lista: ')
    print('4. Sair')
    print('-='*35)
    
    opcao = input('Escolha um numero de (1-4): ')
    
    if opcao == '1':
     nome = input('Nome do contato: ').capitalize()
     numero = input('Numero de telefone: ')
     meu_dicionario[nome] = numero
     print('-'*70)
     print()
     print('Adicionado a lista.')
     
    if opcao == '2':
        nome = input('Contato que deseja remover: ').capitalize()
        remover_contato = meu_dicionario.pop(nome)
        print(f'Nome: {nome}, numero: {remover_contato} removido!!!')
        
    if opcao == '3':
        print(f'Lista atual: {meu_dicionario}')
        
    if opcao == '4':
        print('Finalizando programa!!')
        break
    
    
    
    