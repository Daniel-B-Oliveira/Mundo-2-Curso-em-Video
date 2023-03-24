# 065 - Crie um programa que leia vários números inteiros pelo teclado.
#       No final da execução, mostre a média entre todos os valores
#       e qual foi o maior e o menor valores lidos.
#       O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
c = n = p = g = s = 0
f = 'S'

print('Digite vários valores para que sejam feita sua média')

while f not in 'N':
    n = int(input(''))
    s += n
    c += 1
    if c == 1:
        g = n
        p = n
    else:
        if n >= g:
            g = n
        if n <= p:
            p = n
    f = str(input('continuar? [\033[32mS\033[m/\033[31mN\033[m] ')).strip().upper()
    if f == '':
        f = 'S'

print(f'\nMENOR: \033[31m{p}\033[m\nMAIOR: \033[32m{g}\033[m'
      f'\nMÉDIA(\033[36m{c}\033[m) = \033[36m{s/c:.2f}\033[m')
