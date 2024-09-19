# Crie um programa que receba um número do usuário e exiba a tabuada desse número de 1 a 10.
numero = int(input("Digite um número "))

n2 = 0
for n in range(1,11):
    n2 = n2+1
    print(f'{numero}*{n2}')