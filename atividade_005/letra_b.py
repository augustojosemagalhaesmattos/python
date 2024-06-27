# Evolua o programa anterior para
# um código que pergunte ao usuário qual
# o intervalo que ele deseja ver impresso.

import os


os.system('cls')

print('-'*70)
print('Exercicio Letra B')
print('-'*70)
print('De 1 a 100, qual intervalo você deseja ver impressa: ')
print('='*70)

for var_iteradora in range(1, 101):

    numero = int(input('Digite um número [1-100]: '))


    if numero >= 1 and numero <= 100:
     print(f'O numero {numero} está dentro do intervalo. ')
    else:
        print(f'"{numero}" numero invalido!!')
        
   
   
   
   
   
   

