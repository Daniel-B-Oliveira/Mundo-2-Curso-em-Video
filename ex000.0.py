#  if
#  else + if = elif (um ou mais de um em em uma suceção do mesmo comando)
# else (apens um em uma suceção do mesmo comando)

num = int(input('Digite um núemro'))

if num == 0:
    print('O seu número foi zero, logo ele tambem é par')
elif num == 22 or num == 13:
    print('hum...')
elif num % 2 == 0:
    print(f'Seu número({num}) é par')

else:
    print(f'O seu número({num}) não é par')

