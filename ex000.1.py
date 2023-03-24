#  036: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
#       Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
#       A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado

val = float(input('Qual o valor da casa? '))
sal = float(input('Qual o seu salário? '))
ano = float(input('Em quantas anos será o financiamento? '))

if val / (ano * 12) < sal * 0.3:
    print(f'O seu empréstimo foi \033[32maprovado\033[m, serão {ano} parcelas de R${val/(ano*12)}.')
else:
    print('O seu empréstimo passou por análise, resultando em \033[31mnão provado\033[m.')
