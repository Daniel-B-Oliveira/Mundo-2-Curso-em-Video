# 038 - Escreva um programa que leia dois números inteiros e compare-os.
#       mostrando na tela uma mensagem:
#           O primeiro valor é maior
#           O segundo valor é maior
#           Não existe valor maior, os dois são iguais

a = int(input('Digite um número inteiro: '))
b = int(input('Digite mais um número inteiro:  '))

if a > b:
    print(f'\033[31m{a}\033[m é o maior valor, logo, \033[32m{b}\033[m é o menor valor')
elif a < b:
    print(f'\033[32m{b}\033[m é o mvaior valor, logo \033[31m{a}\033[m é o menor valor')
else:
    print(f'Ambos os valores \033[36m{a, b}\033[m são iguais, logo, não há um valor maior que outro')
