# 041 - A Confederação Nacional de Natação precisa de um programa que
#       leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
#           – Até 9 anos: MIRIM
#           – Até 14 anos: INFANTIL
#           – Até 19 anos: JÚNIOR
#           – Até 25 anos: SÊNIOR
#           – Acima de 25 anos: MASTER

idade = int(input('Qual a sua idade? '))

if idade <= 9:
    print('Você pertence a categoiria, de natação, \033[36mMIRIM\033[m')
elif idade <= 14:
    print('Você pertence a categoiria, de natação, \033[34mINFANTIL\033[m')
elif idade <= 19:
    print('Você pertence a categoiria, de natação, \033[35mJÚNIOR\033[m')
elif idade <= 25:
    print('Você pertence a categoiria, de natação, \033[33mSENIOR\033[m')
else:
    print('Você pertence a categoiria, de natação, \033[31mMASTER\033[m')
