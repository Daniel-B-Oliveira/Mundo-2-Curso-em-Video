# 069 - Crie um programa que leia a idade e o sexo de várias pessoas.
#       A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
#       No final, mostre:
#       A) quantas pessoas tem mais de 18 anos.
#       B) quantos homens foram cadastrados.
#       C) quantas mulheres tem menos de 20 anos.
from datetime import datetime
c = a = s = m = 0
d = datetime.now().year

while True:
    c += 1
    print(f'-=-=-=-=-= {c}ª pessoa =-=-=-=-=-')

    while True:
        ano = int(input('Ano de nascimento: '))
        if d - ano <= 125 and ano <= d:
            break
        elif d - ano > 125:
            print('\n\033[31mData muito antiga, tente outra.\033[m\n')
        elif ano > d:
            print('\n\033[31mEsta data ainda não existe, tente outra.\033[m\n')

    while True:
        sex = str(input('Sexo [F/M] ? ')).strip().upper()[0]
        if sex == 'F' or sex == 'M':
            break
        else:
            print('\n\033[31mValor Impossível, tente outro.\033[m\n')
    if (ano + 18) <= d:
        a += 1
    if sex == 'M':
        s += 1
    if sex == 'F' and d - ano < 20:
        m += 1

    while True:
        print(f'\n{"-="*15}')
        prg = str(input(f'Deseja Continuar [\033[32mS\033[m/\033[31mN\033[m] ? ')).strip().upper()
        print(f'{"-="*15}\n')
        if prg == '':
            prg = 'S'
        if prg == 'N' or prg == 'S':
            break
        else:
            print('\n\033[31mValor Impossível, tente outro.\033[m\n')

    if prg == 'N':
        print('\n\033[31mPrograma será finalizado.\033[m\n')
        break

print(f'\n{"-="*15}')
print(f'-Pessoas com mais de 18 anos: (\033[36m{a}\033[m).')
print(f'-Homnes que foram cadastrados: (\033[36m{s}\033[m).')
print(f'-Mulheres cem menos de 20 anos: (\033[36m{m}\033[m).')
print(f'{"-="*15}')
