# 049 - Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher,
#       só que agora utilizando um laço for.

num = int(input('Escolha um número inteiro: '))
prg = int(input('Escolha entre manter a tabuada até o 10 ou alterar:\n[1]Manter\n[2]Alterar\n[3]Intervalo\n'))
if prg == 1:
    print('')
    for c in range(1, 11):
        print(f'{num} X {c:{2}} = {num*c}')
elif prg == 2:
    m = int(input('Qual será o novo valor? '))
    print(f'\nValor alterado de 10 para {m}\n')
    for c in range(1, m+1):
        print(f'{num} X {c:{len(str(m))}} = {num*c}')
elif prg == 3:
    m0 = int(input('Qual será o valor minímo? '))
    m1 = int(input('Qual será o valor máximo? '))
    print(f'\nValor alterado de 10 para entre {m0} e {m1}\n')
    for c in range(m0, m1+1):
        print(f'{num} X {c:{len(str(m1))}} = {num*c}')
else:
    print(f'\033[31m{prg} é um Valor Impossível\033[m ')
