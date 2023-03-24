# 048 - Faça um programa que calcule a soma entre todos os números
#       que são múltiplos de três e que se encontram no intervalo de 1 até 500.

m = int(input('Até que número será realizada a operação? '))
n = int(input('Qual multiplo você deseja? '))
prg = int(input('Quais valores você deseja? \n[1]Apenas Impares\n[2]Apenas Pares\n[3]Impares e Pares\n'))
p = 0
cnt = 0

if prg == 1:
    if n % 2 != 0:  # [1]Apenas Impares
        for c in range(n, m+1, n*2):  # Múltiplo impar
            p += c
            cnt += 1
        print(f'\nA soma dos {cnt} múltiplos impares de {n} são = {p}')
    elif n % 2 == 0:  # Múltiplo par
        print('\033[31mImpossível, o múltiplo não é impar\033[m')
elif prg == 2:  # [2]Apenas Pares
    if n % 2 != 0:  # Múltiplo impar
        for c in range(n*2, m+1, n*2):
            p += c
            cnt += 1
        print(f'\nA soma dos {cnt} múltiplos impares de {n} são = {p}')
    elif n % 2 == 0:  # Múltiplo par
        for c in range(n, m+1, n):
            p += c
            cnt += 1
        print(f'\nA soma dos {cnt} múltiplos pares de {n} são = {p}')
elif prg == 3:  # [3]Impares e Pares
    for c in range(n, m + 1, n):
        p += c
        cnt += 1
    print(f'\nA soma dos {cnt} múltiplos de {n} são = {p}')
else:
    print(f'\033[31m{prg} é um valor Impossível.\033[m')
