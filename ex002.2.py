# 058 - Melhore o jogo do DESAFIO 28 onde o computador vai “pensar”
#       em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar,
#       mostrando no final quantos palpites foram necessários para vencer.

from random import randint

n0 = randint(0, 10)
c = 1
t = 2
n1 = 11

while n1 not in range(0, 11):
    print(f'CHANCES: \033[36m{t+1}\033[m')
    n1 = int(input('Escolha um número de 0 a 10: '))
    if n1 not in range(0, 11):
        print('\033[31m!!!Escolha um número no alcance!!!\033[m')

while n0 != n1:
    if n1 in range(0, 11):
        print(f'CHANCES: \033[36m{t}\033[m')

        if n0 < n1:
            n1 = int(input('Escolha um número menor: '))

        elif n0 > n1:
            n1 = int(input('Escolha um número maior: '))
        c += 1
        t -= 1

        if t == 0:
            break

    else:
        while n1 not in range(0, 11):
            print('\033[31m!!!Escolha um número no alcance!!!\033[m')
            n1 = int(input('Escolha outro número: '))

if t != 0:

    if c == 1:
        print(f'\nParabéns você acertou de primeira')

    elif c > 1:
        print(f'\nParabéns você acertou em {c} tentativas')
    print(f'\033[36mO número era {n0}.\033[m')

else:
    print('\n\033[31mFim de Jogo, você PERDEU.\033[m')
    print(f'\033[36mO número era {n0}.\033[m')
