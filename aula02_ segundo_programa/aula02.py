# importando a biblioteca de sistema
import os


# Limpando o terminal 
os.sysrem('cls')

print('-')*70 # firula
print('Estudo de variaveis')
print('=')*70 #firula

# As variaveis são declaradas por infêrencia
nome = 'Jonh Doe'
nascimento = 1970
altura = 1.80 
peso = 75.5
doador = True
complexo = 3j # Python trabalha diretamente com números complexos
PI = 3.14 # Isso é uma CONSTANTE, seu valor não deve ser alterado

# Saida utulizando o método type() para verificar o
# tipo da variável
print('\033[0M \033[31mTipos declarados:\033[0m')
print('\033[0m A var \033[0mé do tipo: ', type(nome))
print('\033[0m A var \033[32m nascimento \033[0m é do tipo: ', type(nascimneto))
print('s\033[0m A var \033[32m nascimento \033[0m é do tipo: ', type(nascimento))