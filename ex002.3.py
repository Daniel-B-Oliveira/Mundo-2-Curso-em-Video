# 059 - Crie um programa que leia dois valores e mostre um menu na tela:
#       [ 1 ] somar
#       [ 2 ] multiplicar
#       [ 3 ] maior
#       [ 4 ] novos números
#       [ 5 ] sair do programa

from time import sleep
c0 = int(4)
c1 = 0
c2 = 0


while c0 != 6:
    if c0 == 4:
        c1 = float(input('Escolha um número: '))
        c2 = float(input('Escolha mais outro número: '))
        c0 = 0
    elif c0 == 0:
        c0 = int(input('\033[32mMenu de opções:\033[m'
                       '\n[ 1 ] somar'
                       '\n[ 2 ] multiplicar'
                       '\n[ 3 ] maior'
                       '\n[ 4 ] novos números'
                       '\n[ 5 ] sair do programa \n'))
    elif c0 == 1:
        print(f'{c1} + {c2} = {c1 + c2}\n')
        c0 = 0
        sleep(1)
        prg = str(input('Aperte [S] se deseja continuar. ')).strip().upper()
        if prg == str('S'):
            c0 = 0
        else:
            c0 = 5
        sleep(0.5)
    elif c0 == 2:
        print(f'{c1} * {c2} = {c1 * c2}\n')
        c0 = 0
        sleep(1)
        prg = str(input('Aperte [S] se deseja continuar. ')).strip().upper()
        if prg == str('S'):
            c0 = 0
        else:
            c0 = 5
        sleep(0.5)
    elif c0 == 3:
        if c1 > c2:
            print(f'{c2} < {c1}\n')
            c0 = 0
            sleep(0.5)
            prg = str(input('Aperte [S] se deseja continuar. ')).strip().upper()
            if prg == str('S'):
                c0 = 0
            else:
                c0 = 5
            sleep(0.5)
        else:
            print(f'{c1} < {c2}\n')
            c0 = 0
            sleep(0.5)
            prg = str(input('Aperte [S] se deseja continuar. ')).strip().upper()
            if prg == str('S'):
                c0 = 0
            else:
                c0 = 5
            sleep(0.5)
    elif c0 == 4:
        print('\033[33mNúmeros resetados.\033[m\n')
    elif c0 not in range(1, 6):
        sleep(0.5)
        print('\033[31mOPÇÃO INVÁLIDA, TENTE NOVAMENTE\033[m')
        c0 = 0
        sleep(0.5)
    elif c0 == 5:
        print('\n\033[31mO programa sera finalizado.\033[m')
        sleep(0.5)
        c0 = 6
