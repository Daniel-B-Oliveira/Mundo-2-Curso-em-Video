# 060 - Faça um programa que leia um número qualquer e mostre o seu fatorial.
# from math import factorial
# num2 = factorial(int(input('Digite um número para que seja calculado seu fatorial: ')))
# print(num2)

cont = num0 = 1
num1 = int(input('Digite um número para que seja calculado seu fatorial: '))
if num1 == 0:
    num1 = 1
while num0 != num1:
    cont *= (num0+1)
    num0 += 1

'''for num0 in range(1, num1+1):
    cont *= num0
    num0 += 1'''

print('\n', cont)
