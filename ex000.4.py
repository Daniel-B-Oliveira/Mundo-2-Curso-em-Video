# 039 - Faça um programa que leia o ano de nascimento de um jovem e informe,
#       de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
#       se é a hora exata de se alistar ou se já passou do tempo do alistamento.
#       Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

a = date.today().year

ano = int(input('Em que ano você nasceu? '))

if date.today().year - ano < 18:
    print(f'\n\033[32mVocê não chegou na idade de se alistar (18 anos).\n'
          f'Ainda faltam {18 -(date.today().year - ano) } anos(s), '
          f'seu alistamento será em {ano+18}.\033[m')
elif date.today().year - ano == 18:
    print(f'\n\033[33mEste é o ano do seu alistamento ({date.today().year}).\033[m')
else:
    print(f'\n\033[31mVocê já passou da data do alistamento ({ano+18}) '
          f'em {date.today().year - (ano+18)} ano(s).\033[m')