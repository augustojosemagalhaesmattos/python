import os


os.system('cls')



def calcular_distancia_metros(metros, minutos):
    # converter min para segundos
  minutos = minutos * 60
    # calcular distancia metros
  distancia_metros = metros * minutos
  return distancia_metros

metros = float(input('Digite a distacia percorrida (em metros):'))
minutos = float(input('Digite o tempo gasto (em minutos): '))

print(f'A velocidade media é {minutos} metros por minuto.')