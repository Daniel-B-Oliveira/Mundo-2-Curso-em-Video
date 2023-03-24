# 070 - Crie um programa que leia o nome e o preço de vários produtos.
#       O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
#       A) qual é o total gasto na compra.
#       B) quantos produtos custam mais de R$1000.
#       C) qual é o nome do produto mais barato.
from time import sleep
b = t = 1
c = p = s = 0
nome = ''

while True:
    prod = str(input('PRODUTO: ')).strip().title()
    valor = float(input('PREÇO: R$'))

    if s == 0:
        p = valor
        nome = prod
    s += valor
    if valor <= p:
        b = valor
        nome = prod
    if valor > 1000:
        c += 1

    while True:
        print(f'\n{"~" * 35}')
        prg = str(input('Deseja continuar [\033[32mS\033[m/\033[31mN\033[m] ')).strip().upper()
        print(f'\n{"~" * 35}')
        if prg == '':
            prg = 'S'
        if prg in 'SN':
            break
        else:
            print('\n\033[31mValor Impossível, Tente Outro.\033[m')

    if prg == 'N':
        print('\033[34mFinalizando\033[m', end='')
        for t in range(1, 4):
            if t == 3:
                sleep(0.7)
                print('\033[34m.\033[m')
            else:
                sleep(0.7)
                print('\033[34m.\033[m', end='')
        break

print(f'{"~"*35}\n')
print(f'\033[0;4m{c}\033[m produto(s) acima de R$1000.00.')
print(f'Produto mais barato: {nome}(R${b:.2f})')
print(f'TOTAL: \033[36mR${s:.2f}\033[m')
print(f'\n{"~"*35}')

print()