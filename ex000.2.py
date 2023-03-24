# 037 - Escreva um programa em Python que leia um número inteiro qualquer
#       e peça para o usuário escolher qual será a base de conversão:
#       1 para binário
#       2 para octal e
#       3 para hexadecimal

num0 = int(input('Escreva um número inteiro: '))
opt = int(input('\033[31m[1]\033[m converter para BINÁRIO\n'
                '\033[32m[2]\033[m converter para OCTAL\n'
                '\033[33m[3]\033[m converter para HEXADECIMAL\n'))
if opt == 1:
    print(f'Número \033[36m{num0}\033[m convertido em binário: \033[31m{bin(num0)[2:]}\033[m')
elif opt == 2:
    print(f'Número \033[36m{num0}\033[m convertido em octal: \033[32m{oct(num0)[2:]}\033[m')
elif opt == 3:
    print(f'Número \033[36m{num0}\033[m convertido em hexadecimal: \033[33m{hex(num0)[2:]}\033[m')
else:
    print('\033[4;31mOpção inválida.\033[m')
