# 053 - Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
#       desconsiderando os espaços. Exemplos de palíndromos

fra0 = str(input('Digite uma frase: ')).replace(' ', '').replace('', ' ').strip().lower()
'''cont = 0
for c in range(0, len(fra0.split())-1):
    if fra0.split()[len(fra0.split())-c-1] != fra0.split()[c]:
        cont += 1
if cont == 0:
    print('\n\033[32mÉ um palíndromo\033[m')
elif cont > 1:
    print('\n\033[31mNão é um palíndromo\033[m')'''

fra1 = fra0.split()
fra2 = fra1[::-1]
if fra1 == fra2:
    print('\n\033[32mÉ um palíndromo\033[m')
else:
    print('\n\033[31mNão é um palíndromo\033[m')
