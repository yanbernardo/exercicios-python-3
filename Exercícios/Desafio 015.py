km = float(input('Quantos KMs foram rodados com o veículo?: '))
d = int(input('Por quantos dias ele foi alugado?: '))
p = 60 * d + 0.15 * km
print('Com {}KMs rodados por {} dias, o preço do aluguel foi de R${:.2f}'.format(km, d, p))
