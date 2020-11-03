r1 = float(input('Digite o tamanho do primeiro lado:\n'))
r2 = float(input('Digite o tamanho do segundo lado:\n'))
r3 = float(input('Digite o tamanho do terceiro lado:\n'))
if abs(r1 - r2) < r3 < r1 + r2:
    print('As 3 retas formam um triangulo!')
else:
    print('As 3 retas NÃO formam um triangulo!')