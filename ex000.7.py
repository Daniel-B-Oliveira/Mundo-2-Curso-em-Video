# 042 - Refaça o DESAFIO 35 dos triângulos,
#       acrescentando o recurso de mostrar que tipo de triângulo será formado:
#           – EQUILÁTERO: todos os lados iguais
#           – ISÓSCELES: dois lados iguais, um diferente
#           – ESCALENO: todos os lados diferentes

a = float(input('Insira o comprimento do primero lado do triângulo: '))
b = float(input('Insira o comprimento do segundo lado do triângulo: '))
c = float(input('Insira o comprimento do teceiro lado do triângulo: '))

if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print('\n\033[36mAs retas podem formar um triângulo equilátero\033[m')
    elif a == b or a == c or b == c:
        print('\n\033[35mAs retas podem formar um triângulo isóceles\033[m')
    else:
        print('\n\033[34mAs retas podem formar um triângulo escaleno\033[m')
else:
    print('\n\033[31mAs retas não podem formar um triângulo\033[m')
