import os


os.system('cls')


# Entrada
a = float(input('Digite o valor do 1ª lado: '))
b = float(input('Digite o valor do 2ª lado: '))
c = float(input('Digite o valor do 3ª lado: '))

# Processo
if a + b > c and a + c > b and b + c > a:
    
    print("Os segmentos podem formar um triângulo.")
else:
    print("Os segmentos não podem formar um triângulo.")
