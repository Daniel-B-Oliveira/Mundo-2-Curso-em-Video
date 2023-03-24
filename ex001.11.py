# 056 - Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
#       No final do programa, mostre: a média de idade do grupo,
#       qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

soma = 0
idadem = 0
nomem = str('"mNão Houve"')
cont = 0

for c in range(1, 5):
    print(str(f'----- {c}ª Pessoa -----'))
    nome = str(input(f'NOME: '))
    idade = int(input(f'IDADE: '))
    sexo = str(input(f'SEXO [M/F]')).strip().upper()
    soma += idade
    if sexo == 'M':
        if idade > idadem:
            idadem = idade
            nomem = nome
    elif sexo == 'F':
        if idade < 20:
            cont += + 1
    elif sexo != 'M' and sexo != 'F':
        print(f'\033[31m{sexo} é um Valor Impossível\033[m')

print(f'\nA média de idade do grupo é {soma/4}'
      f'\nO homem mais velho, com {idadem} anos, se chama {nomem.strip().title()}'
      f'\nO número de mulheres com menos de 20 anos é {cont}')
