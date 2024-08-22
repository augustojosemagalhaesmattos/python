import os


class Banco():
    def __init__(self, nome='', agencia=0, conta=0, cpf=0,
                 conta_corrente=0, poupanca=0):
        self.nome = nome
        self.agencia = agencia
        self.conta = conta
        self.cpf = cpf
        self.conta_corrente =  conta_corrente
        self.poupanca = poupanca
        
    def deposito(self, valor):
        escolha = input(
            'Conta Corrente (cc) ou Poupaça (po)? ').lower().strip()
        
        if escolha == 'cc':
            print(f'Valor do deposito: (+)R${valor}')
            print(f'Saldo anterior (CC): R${self.conta_corrente}')
            self.conta_corrente += valor
            print(f'\tSaldo atual na Conta Corrente: R${self.conta_corrente}')
            print('-'*70)
            
        elif escolha == 'po':
            print(f'\nValor do deposito: (+)R${valor}')
            print(f'\Saldo anterior na Poupança: R${self.poupanca}')
            self.poupanca += valor
            print(f'Saldo atual na Poupança: R${self.poupanca}')
            print('-'*70)
            
        else:
            print('Opção invalida')
        
    def saque(self, valor):
        escolha = input(
            'Conta corrente (cc) ou Poupança (po)? ').lower(). strip()
        
        if escolha == 'cc':
          print(f'\nValor sacado: (-)R${valor}')
          print(f'\Saldo anterior na CC: R${self.conta_corrente}')
          self.conta_corrente -= valor
          print(f'\tSaldo Atual ma CC: R${self.conta_corrente}')
          print('-'*70)
          
        elif escolha == 'po':
            print(f'\nValor sacado: (-)R${valor}')
            print(f'\Saldo anterior em Poupança: R${self.poupanca}')
            self.poupanca -= valor
            print(f'\tSaldo Atual na Poupança: R${self.poupanca}')
            print('-'*70)
            
        else:
            print('Opção invalida!')
            
        
os.system('cls')

# Coletar dados do usúario para criar uma nova conta
print('Digite os dados para criar uma nova conta: ')
nome = input('Nome: ')
agencia = int(input('Número da Conta: '))
conta = int(input('Número da Conta: '))
cpf = int(input('CPF: '))
conta_corrente =  float(input('Saldo inicial da Conta Corrente: '))
poupanca = float(input('Saldo inicial da Poupança: '))

# Criar um novo correntista
correntista = Banco(nome, agencia, conta, cpf, conta_corrente, poupanca)


print('-'*70)
print('Movimentação Bancária')
print('='*70)
opcao = input('Deposito ou saque (D/S)? ').upper().strip()

if opcao == 'D':
    valor = float(input('Qual o valor do depositar? '))
    correntista.deposito(valor)
    
elif opcao == 'S':
    valor = float(input('Qual o valor do saque? '))
    correntista.saque(valor)
    
else:
    print('Opção Inválida')
          
    
          
      
        
        
       
        
        
        
        
        
        
        
