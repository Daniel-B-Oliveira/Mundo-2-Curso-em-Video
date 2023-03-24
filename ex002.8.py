# 064 - Crie um programa que leia vários números inteiros pelo teclado.
#       O programa só vai parar quando o usuário digitar o valor 999,
#       que é a condição de parada. No final, mostre quantos números
#       foram digitados e qual foi a soma entre eles (desconsiderando o flag).
c = num1 = 0
num0 = int(input('\033[31m[999] Para pausar as somas\033[m\nDigite vários números para vermos o total da soma:\n'))
while num0 != 999:
    num1 += num0
    c += 1
    num0 = int(input())
print(f'TOTAL(\033[36m{c}\033[m): {num1}')
