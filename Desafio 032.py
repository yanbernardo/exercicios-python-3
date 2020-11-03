print('Calculadora de ANOS BISSEXTOS')
year = int(input('Digite o ano para saber se ele é bissexto\n'))
if year % 4 == 0:
    print('{} é BISSEXTO!'.format(year))
else:
    print('{} NÃO é BISSEXTO!'.format(year))