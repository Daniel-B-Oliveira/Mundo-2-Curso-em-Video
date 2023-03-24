# 047 - Crie um programa que mostre na tela todos os números pares
#       que estão no intervalo entre 1 e 50.

n = int(input('Até qual numero será feita uma lista apenas com pares? '))
for c in range(0, n+1, 2):
    if c == n:
        print(c, end='.')
    else:
        print(c, end=', ')
