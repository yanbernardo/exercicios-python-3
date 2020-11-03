v = float(input('Qual a velocidade do veículo?\n'))
if v > 80:
    multa = (v - 80) * 7
    print('Você foi multado em R${:.2f}'.format(multa))
else:
    print('Você está dentro do limite de velocidade.')