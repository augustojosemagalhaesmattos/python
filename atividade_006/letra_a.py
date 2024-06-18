import os


os.system('cls')

print('-'*70)
print('Exercicio Letra A ')
print('-'*70)

lista = [1, 2, 3, 5, 6]


valor_faltando = 4

posicao_correta = 3
lista.insert(posicao_correta, valor_faltando)

print(f"Lista atualizada:", lista)