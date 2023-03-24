# 040  Crie um programa que leia duas notas de um aluno e calcule sua média,
#       mostrando uma mensagem no final, de acordo com a média atingida:
#           – Média abaixo de 5.0: REPROVADO
#           – Média entre 5.0 e 6.9: RECUPERAÇÃO
#           – Média 7.0 ou superior: APROVADO

a = float(input('Qual a sua primeira nota? '))
b = float(input('Qual a sua segunda nota? '))

if (a+b)/2 >= 7:
    print(f'\nMédia: {(a+b)/2:.1f}\n\n\033[32mAluno aprovado\033[m')
elif (a+b)/2 < 5:
    print(f'\nMédia: {(a+b)/2:.1f}\n\n\033[31mAluno reprovado\033[m')
else:
    print(f'\nMédia: {(a + b) / 2:.1f}\n\n\033[33mAluno em recuperação\033[m')
