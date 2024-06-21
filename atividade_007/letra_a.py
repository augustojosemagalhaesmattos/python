# Faça um programa que leia um número indeterminado de notas (pressione ‘s’ ou ‘0’ para sair). 
# Após esta entrada de dados, faça o seguinte:
# • Mostre a quantidade de notas que foram lidas.
# • Exiba todas as notas na ordem em que foram informadas.
# • Exiba todas as notas na ordem inversa à que foram informadas, uma abaixo da outra.
# • Calcule e mostre a soma das notas.
# • Calcule e mostre a média das notas.
import os


os.system('cls')

print('-'*70)
print('Exercicio letra A')
print('-'*70)

notas = []

while True:
    nota_str = input("Digite uma nota (ou 's' para sair, '0' para parar): ")
    
    if nota_str.lower() == 's':
        break
    elif nota_str == '0':
        break
    
    nota = float(nota_str) 
    notas.append(nota)


print(f"\nQuantidade de notas lidas: {len(notas)}")

print("\nNotas na ordem informada:")
for nota in notas:
    print(nota)

print("\nNotas na ordem inversa:")
for nota in reversed(notas):
    print(nota)


soma = sum(notas)
print(f"\nSoma das notas: {soma}")

if len(notas) > 0:
    media = soma / len(notas)
    print(f"Média das notas: {media:.2f}")
else:
    print("Não foi possível calcular a média, pois não há notas inseridas.")


