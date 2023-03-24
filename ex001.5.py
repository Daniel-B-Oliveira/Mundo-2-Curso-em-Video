# 050 - Desenvolva um programa que leia seis números inteiros e
#       mostre a soma apenas daqueles que forem pares.
#       Se o valor digitado for ímpar, desconsidere-o
soma = 0
cont = 0
p = str('Inimigo da PEP')
prg = int(input('\n\033[36mEscolha quantas perguntas serão feitas:\033[m '))
print('')
for c in range(1, prg+1):
    p = int(input(f'Digite o {c:{len(str(prg))}}° número: '))
    if p % 2 == 0:
        soma += p
        cont += 1

if prg != 1 and prg != 0:
    if cont == 1:
        print(f'\nDos {prg} valores, {cont} é par.\nSendo este o valor: \033[31m{soma}\033[m')
    elif cont == prg:
        print(f'\nDos {prg} valores, todos.\nEstes núemros somados resultam em : \033[31m{soma}\033[m')
    else:
        print(f'\nDos {prg} valores, {cont} são pares.\nEstes núemros somados resultam em : \033[31m{soma}\033[m')
elif prg == 1:
    if cont == 1:
        print(f'{p} é Par.')
    else:
        print(f'{p} não é Par ')
else:
    print(f'\033[31m{prg} é um Valor Impossível\033[m')
