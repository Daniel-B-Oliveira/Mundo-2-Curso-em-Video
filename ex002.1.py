# 057 - Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’.
#       Caso esteja errado, peça a digitação novamente até ter um valor correto

s = str('S')
while s not in 'MmFf':
    s = str(input('Digite seu sexo: [M/F]')).strip()[0]
    if s not in 'MmFf':
        print('\033[31mResposta Inválida, a mensagem será repetida\033[m')
if s in 'Mm':
    s = 'Masculino'
else:
    s = 'Feminino'
print(f'\nSeu sexo é \033[36m{s}\033[m.')
