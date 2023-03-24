s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    else:
        s += n
print(f'SOMA: {s}')
