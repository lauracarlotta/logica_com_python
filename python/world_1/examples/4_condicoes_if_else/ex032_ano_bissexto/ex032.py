# Faça um programa que leia um ano qualquer e mostre se ele é um ano Bissexto!

year = int(input('Informe um ano: '))

if year % 4 == 0:
    print(f'{year},  ESSE É UM ANO BISSEXTO!')

else:
    print(f'{year}, Esse é um ano normal!')
