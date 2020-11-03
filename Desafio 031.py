km = float(input('Qual é a distância do seu destino?\n'))
if km <= 200:
    print('O valor de sua passagem é de R${:.2f}.'.format(km * 0.5))
else:
    print('O valor de sua passagem é de R${:.2f}.'.format(km * 0.45))
print('Boa Viagem!!')