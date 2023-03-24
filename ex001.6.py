# 051 - Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
#       No final, mostre os 10 primeiros termos dessa progressão.

n1 = int(input('Qual será o primeiro termo desta PA? '))
rz = int(input('Qual é a razão da PA?'))
prg = int(input('Quantos termos terão esta PA? '))
cont = 0

for c in range(n1, (n1+(prg-1)*rz)+1, rz):
    if c == n1+(prg-1)*rz:
        print(c, end='.')
    else:
        print(c, end=' - ')
