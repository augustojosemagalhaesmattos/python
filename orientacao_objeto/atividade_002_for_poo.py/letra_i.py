# Faça um algoritmo que imprima a frase "estou em looping" 
# e, em seguida, solicite ao usuário digitar uma letra.
# Caso a letra seja o “f" finalize a aplicação.
# Do contrário, imprima novamente a mesma frase até que
# o caractere “f" seja digitado.

import os


os.system('cls')

class Looping:
    def __init__(self,f):
        self.f = f
    
    def parar(self, f):
        pass
    
class Algoritmo(Looping):
    def __init__(self, f):
        self.f = f
        
    def parar(self):
         
         while True:
             sair = input('Estou em looping, digite "f" para sair: ').lower()
             print('-'*70)

             if sair == 'f':
                 print('looping finalizado')
                 break
             
algoritmo = Algoritmo('f')
resultado = algoritmo.parar()
            
             
             
             
        
             
        
    
    

