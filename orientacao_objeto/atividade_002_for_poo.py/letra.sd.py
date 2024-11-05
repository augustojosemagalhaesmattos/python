# Faça um programa que verifique se o usuário e senha
# estão inseridos em um banco de dados (fake). O usuário
# só terá acesso se digitar os dados corretos e, assim, sair
# do laço.
import os


class BancoDados:
    def __init__(self, usuario, senha):
        self.senha = senha
        self.usuario = usuario
        
    def analise(self, senha, usuario):
        pass
    
class Analise_De_Dados:
     def __init__(self, usuario, senha):
        self.senha = senha
        self.usuario = usuario
        
     def analise(self):
        
        while True:
            
            if self.usuario == 'augusto' and self.senha == '2745':
                print('Login realizado com sucesso! ')
                break
            else:
                print('Erro')
                self.usuario = input('Digite o nome de usuario: ')
                self.senha = input('Digite a senha: ')  
                
                
                
            
            
                
usuario = input('Digite o nome de usuario: ')
senha = input('Digite a senha: ')          
bancodados = Analise_De_Dados(usuario, senha)
bancodados.analise()
            
        

        
    
