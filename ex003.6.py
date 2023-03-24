# 071 - Crie um programa que simule o funcionamento de um caixa eletrônico.
#       No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
#       e o programa vai informar quantas cédulas de cada valor serão entregues.
#       OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

cin = vin = dez = uni = 0

val = int(input('Valor do Saque: R$'))

while True:
    if val - 50 >= 0:
        val -= 50
        cin += 1
    else:
        if val - 20 >= 0:
            val -= 20
            vin += 1
        else:
            if val - 10 >= 0:
                val -= 10
                dez += 1
            else:
                if val - 1 >= 0:
                    val -= 1
                    uni += 1
                else:

                    break

n = len(str(cin))
print(f'\n{cin:{n}} - \033[31mR$50.00\033[m')
print(f'{vin:{n}} - \033[32mR$20.00\033[m')
print(f'{dez:{n}} - \033[33mR$10.00\033[m')
print(f'{uni:{n}} - \033[34mR$01.00\033[m')
