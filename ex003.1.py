# 066 - Crie um programa que leia números inteiros pelo teclado.
#       O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
#       No final, mostre quantos números foram digitados e qual foi a soma entre elas
#       (desconsiderando o flag).
num = c = s = 0
while True:
    num = int(input('Digite um número inteiro [\033[31m999 STOP\033[m]: '))
    if num == 999:
        break
    c += 1
    s += num
print(f'\nSOMA(\033[36m{c}\033[m): {s}')
