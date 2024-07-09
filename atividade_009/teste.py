import os


os.system('cls')

meu_dicioanrio = {}

while True:
    print('1. Digite o contato e o numero de telefone: ')
    print('2. Digite o contato que deseja remover: ')
    print('3. Ver lista atualizada: ')
    print('4. Digite (s-sair): ')
    
    opcao = input('Digite um numero (1-6): ')
    
    if opcao == '1':
      nome = input('Digite o nome do contato: ').capitalize()
      numero = input('Numero de telefone: ')
      meu_dicioanrio[nome] = numero
    
    elif opcao == '2':
      remover_numero = meu_dicioanrio.pop()
      nome = input('Contato que deseja remover: ').capitalize()
      print(f'Contato {remover_numero} removido!')
    elif opcao == '3':
        (f'Dicionario atualizado: `{meu_dicioanrio}')
        
    elif opcao == '4':
        if nome == 's':
            print('Programa finalizado!')
            break
        
        
    
    


