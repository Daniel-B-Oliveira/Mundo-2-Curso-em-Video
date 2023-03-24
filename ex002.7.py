# 063 - Escreva um programa que leia um número N inteiro qualquer
#       e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.
c = 3
na = 0
nb = 1
n1 = int(input('Valro de [N]: '))
print(f'{na} - {nb}', end=' - ')
while c <= n1:
    nc = nb + na
    print(f'{nc}', end=' - ')
    na = nb
    nb = nc
    c += 1
print('infinito...')
