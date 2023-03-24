# 046 - Faça um programa que mostre na tela uma contagem regressiva
#       para o estouro de fogos de artifício, indo de 10 até 0,
#       com uma pausa de 1 segundo entre eles.
from time import sleep
n = int(input('Contagem regressiva até 0 '))
for c in range(n, -1, -1):
    print(c)
    sleep(1)

print('BUM! BUM! POOOW!')
