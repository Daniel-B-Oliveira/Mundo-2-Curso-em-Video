# 062 - Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
#       O programa encerrará quando ele disser que quer mostrar 0 termos
cont = 1
tt = 0
tf = 10
t1 = int(input('Qual será o primeiro terma da PA? '))
r = int(input('Qual será a razãoo da PA? '))
print(f'{"-="*25}')
while tf != 0:
    tt += tf
    print(f'\n\033[1;4mPA({cont}, {tf+cont-1})\033[m: ', end='')
    while cont <= tt:
        print(t1, end=' - ')
        t1 += r
        cont += 1
    print('\033[1;4;7mPausa\033[m')
    tf = int(input('\n\n\033[1;4;7mAdicionar termos:\033[m '))
