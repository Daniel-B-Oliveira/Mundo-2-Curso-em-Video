# 068 - Faça um programa que jogue par ou ímpar com o computador.
#       O jogo só será interrompido quando o jogador perder, mostrando o total
#       de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint
c = 0
while True:
    while True:
        prg0 = str(input('PAR [P] ou IMPAR [I] ? ')).strip().upper()[0]
        if prg0 == 'P' or prg0 == 'I':
            break
        else:
            print(f'\033[31mValor Impossível\033[m (\033[36m{prg0}\033[m)')

    while True:
        num0 = int(input('Digite um número de 1 a 10: '))
        if num0 in range(1, 11):
            break
        else:
            print(f'\033[31mValor Impossível\033[m (\033[36m{num0}\033[m)')

    num1 = randint(1, 11)
    div = (num0+num1) % 2

    if div != 0:  # Impar
        if prg0 == 'P':
            print(f'\nPC: IMPAR, {num1}')
            print(f'VC: PAR, {num0}')
            print('\nO Resultado foi IMPAR')
            print('\n\033[31mVocê Perdeu.\033[m\n')
            break
        elif prg0 == 'I':
            c += 1
            print(f'\nPC: PAR, {num1}')
            print(f'VC: IMPAR, {num0}')
            print('\nO Resultado foi IMPAR')
            print('\n\033[32mVocê Ganhou.\033[m\n')
    elif div == 0:  # Par
        if prg0 == 'I':
            print(f'\nPC: PAR, {num1}')
            print(f'VC: IMPAR, {num0}')
            print('\nO Resultado foi PAR')
            print('\n\033[31mVocê Perdeu.\033[m\n')
            break
        elif prg0 == 'P':
            c += 1
            print(f'\nPC: IMPAR, {num1}')
            print(f'VC: PAR, {num0}')
            print('\nO Resultado foi PAR')
            print('\n\033[32mVocê Ganhou.\033[m\n')

print(f'\033[36mVocê Ganhou {c} vezes no total.\033[m')
