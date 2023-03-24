# 055 - Faça um programa que leia o peso de cinco pessoas. No final,
#       mostre qual foi o maior e o menor peso lidos.
p0 = 0
p1 = 0
for c in range(1, 6):
    a = float(input(f'Qual o peso da {c}° pessoa? '))
    if c == 1:
        p0 = a
        p1 = a
    else:
        if a > p0:
            p0 = a
        if a < p1:
            p1 = a
print(f'Maior peso: \033[36m{p0}Kg\033[m\nMenor peso: \033[36m{p1}Kg\033[m')
