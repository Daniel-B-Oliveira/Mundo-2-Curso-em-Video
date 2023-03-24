# 044 - Elabore um programa que calcule o valor a ser pago por um produto,
#       considerando o seu preço normal e condição de pagamento:
#           – à vista dinheiro/cheque: 10% de desconto
#           – à vista no cartão: 5% de desconto
#           – em até 2x no cartão: preço formal
#           – 3x ou mais no cartão: 20% de juros /// alterei para 3% de juros para cada parcela.

valor = float(input('Qual o valor do produto? R$'))
pag = int(input('\nO pagamento será á vista ou parcelado?'
                '\n[1] Á vista.'
                '\n[2] Parcelado (Apenas no cartão)\n'))
if pag == 1:
    p = int(input('\nQual será a forma de pagamento?'
                  '\n[1] Dinheiro.'
                  '\n[2] Cheque.'
                  '\n[3] Cartão.\n'))
    if p == 1:
        print(f'\nO valor da compra em dinheiro ficará em:\n'
              f'R${valor} mais R${valor * 0.1:.2f} de desconto: R${valor * 0.9:.2f}')
    elif p == 2:
        print(f'\nO valor da compra em cheque ficará em:\n'
              f'R${valor:.2f} mais R${valor * 0.1:.2f} de desconto: R${valor * 0.9:.2f}')
    elif p == 3:
        print(f'\nO valor da compra no cartão ficará em:\n'
              f'R${valor:.2f} mais R${valor * 0.05:.2f} de desconto: R${valor * 0.95:.2f}')
    else:
        print(f'\n\033[31mValor desconhecido ({p}).\033[m')
elif pag == 2:
    p = int(input('\nEm quantas vezes serão efetuadas o pagamento? '))
    if p == 1:
        print(f'\nO valor da compra no cartão ficará em:\n'
              f'R${valor:.2f} menos R${valor * 0.05:.2f} de desconto: R${valor * 0.95:.2f}')
    elif p > 1:
        print(f'\nO valor da compra parcelada no cartão ficará em:\n'
              f'{p} parcelas de R${(valor * ( 1.03  ** (p-2)))/p:.2f} = R${valor * ( 1.03  ** (p-2)):.2f}')
    else:
        print(f'\n\033[31mValor desconhecido ({p}).\033[m')
else:
    print(f'\n\033[31mValor desconhecido ({pag}).\033[m')
