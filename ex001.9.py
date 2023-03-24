# 054 - Crie um programa que leia o ano de nascimento de sete pessoas.
#       No final, mostre quantas pessoas ainda não atingiram a maioridade
#       e quantas já são maiores.
from datetime import date
idd = 0
for c in range(1, 8):
    prg = int(input(f'Qual o ano em que a {c}° pessoa nasceu? ')) + 18
    if prg <= date.today().year:
        idd += 1
if idd != 1:
    print(f'\n\033[36m{idd}\033[m pessoas \033[32matingiram\033[m a maioridade.')
elif idd == 1:  # Apenas uma pessoa atingiu a maioridade
    print(f'\n\033[36m{idd}\033[m pessoa \033[32matingiu\033[m a maioridade.')
if 7-idd != 1:
    print(f'\n\033[36m{7-idd}\033[m pessoas \033[31mnão atingiram\033[m a maioridade.')
elif 7-idd == 1:  # Apenas uma pessoa não atingiu a maioridade
    print(f'\n\033[36m{7-idd}\033[m pessoa \033[31mnão\033[m atingiu a maioridade.')
