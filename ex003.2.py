# 067 - Faça um programa que mostre a tabuada de vários números, um de cada vez,
#       para cada valor digitado pelo usuário. O programa será interrompido quando o
#       número solicitado for negativo.
c = num = 0

while True:
    print(f'{"="*30}')
    num = int(input('\nDigite um número: '))
    print(f'\n{"=" * 30}')
    if num <= 0:
        break
    while True:
        c += 1
        print(f'{num} X {c:2} = {num*c}')
        if c == 10:
            c = 0
            break
