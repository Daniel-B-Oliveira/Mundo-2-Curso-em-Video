# 06 - Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA,
#      mostrando os 10 primeiros termos da progressão usando a estrutura while.

cont = 1
t1 = int(input('Qual será o primeiro terma da PA? '))
r = int(input('Qual será a razãoo da PA? '))

while cont <= 10:
    if cont == 1:
        print('PA: ', end='')
    print(t1, end='')
    if cont == 10:
        print('.', end='')
    else:
        print(', ', end='')
    t1 += r
    cont += 1
