import os


os.system('cls')


for c in range(1,8):
  numero =  input('Digite um número [1-7]:')
  
  if (not (numero.isnumeric())):
      print(f'"{numero}" invalido!! ')
      
  else:
      numero = int(numero)
      
      if (numero >= 1 and numero <= 7):
          print(f'"{numero}" Está dentro do intervalo')
          
      else:
          print(f'{numero} nao esta no intervalo')
      