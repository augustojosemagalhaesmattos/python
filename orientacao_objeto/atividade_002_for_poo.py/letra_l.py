# Faça um algoritmo que imprima a frase "estou em looping" e,
# em seguida, solicite ao usuário digitar uma letra. Caso
# a letra seja o “f" finalize a aplicação. Do contrário,
# imprima novamente a mesma frase até que o caractere “f"
# seja digitado.


import os


os.system('cls')


class Looping:
    def __init__(self, sair):
        self.sair = sair
        
    def parar(self, sair):
        pass
    
class Imprimir:
    def __init__(self, sair):
        self.sair = sair
        
    def parar(self):
        while True:
            entrada = input('Estou em looping, digite "f" para sair do looping. ' )
            if entrada == 'f':
                print('Programa finalizado!')
                break
            else:
                print()
                
looping = Imprimir('')
looping.parar()
                
        
    
    
