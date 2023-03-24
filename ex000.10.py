# 045 - Crie um programa que faça o computador jogar Jokenpô com você.
from random import randint

pc = randint(1, 3)
voce = int(input('''Escolha entre pedra, papel e  tesoura
[1] Pedra.
[2] Papel. 
[3] Tesoura\n'''))

if voce <= 3 and voce != 0:
    if pc == voce:
        print('\033[36mVocê empatou com a máquina\033[m')
    else:
        if pc == 1:
            print('A máquina escolheu pedra.\n')
            if voce == 2:
                print('\033[32mVocê Venceu\033[m')
            else:
                print('\033[31mVocê perdeu\033[m')
        elif pc == 2:
            print('A máquina escolehu Papel.\n')
            if voce == 3:
                print('\033[32mVocê Venceu\033[m')
            else:
                print('\033[31mVocê perdeu\033[m')
        elif pc == 3:
            print('A máquina escolehu Tesoura.\n')
            if voce == 1:
                print('\033[32mVocê Venceu\033[m')
            else:
                print('\033[31mVocê perdeu\033[m')
else:
    print('\033[31mValor impossível\033[m')
