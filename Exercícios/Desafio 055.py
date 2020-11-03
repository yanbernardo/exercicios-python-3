max = 0
min = 0
for c in range(1, 6):
    p = float(input('Digite o peso da {}ª pessoa(kg):\n'.format(c)))
    if min == 0:
        min = p
    if p > max:
        max = p
    elif p < min:
        min = p
print('Mais pesado = {}Kg\nMais leve = {}Kg'.format(max, min))
