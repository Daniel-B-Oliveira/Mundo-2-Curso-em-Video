# 043 - Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
#       calcule seu Índice de Massa Corporal (IMC) e mostre seu status,
#       de acordo com a tabela abaixo:
#           – IMC abaixo de 18,5: Abaixo do Peso
#           – Entre 18,5 e 25: Peso Ideal
#           – 25 até 30: Sobrepeso
#           – 30 até 40: Obesidade
#           – Acima de 40: Obesidade Mórbida

peso = float(input('Informe seu peso em Kg: '))
altura = float(input('Informe sua aultua em metros'))

if peso/(altura**2) < 18.5:
    print(f'\n\033[33mVocê esta Abaixo do Peso.'
          f'\nSeu IMC é de {peso/(altura**2):.1f}\033[m')
elif peso/(altura**2) < 25:
    print(f'\n\033[32mVocê esta no Peso Ideal.'
          f'\nSeu IMC é de {peso/(altura**2):.1f}\033[m')
elif peso/(altura**2) < 30:
    print(f'\n\033[33mVocê esta com Sobrepeso.'
          f'\nSeu IMC é de {peso/(altura**2):.1f}\033[m')
elif peso/(altura**2) < 40:
    print(f'\n\033[31mVocê esta com Obsidade.'
          f'\nSeu IMC é de {peso/(altura**2):.1f}\033[m')
else:
    print(f'\n\033[7;31mVocê esta com Obesidade Mórbida.\033[m'
          f'\n\033[7;31mSeu IMC é de {peso/(altura**2):.1f}\033[m')
