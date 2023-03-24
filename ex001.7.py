# 052 - Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

num = int(input('Digite um número inteiro: '))
cont = 0
for c in range(1, num+1):
    if num % c == 0:
        cont += 1
        if cont > 2:
            break
if cont == 2:
    print('\n\033[32mEste número é primo\033[m')
elif cont != 2:
    print(f'\n\033[31mEste número não é primo\033[m')
