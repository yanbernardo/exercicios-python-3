def area(l, c):
    area = l * c
    print(f'O terreno de comprimento {c}m e largura {l}m tem {area}m²')
def titulo(t):
    print('-' * 30)
    print(f'{t:^30}')
    print('-' * 30)


titulo('CALCULO DE ÁREA')
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l, c)

