r1 = float(input('Digite o tamanho do primeiro lado:\n'))
r2 = float(input('Digite o tamanho do segundo lado:\n'))
r3 = float(input('Digite o tamanho do terceiro lado:\n'))
if abs(r1 - r2) < r3 < r1 + r2:
    if r1 == r2 == r3:
        print('As 3 retas \033[1;32mFORMAM\033[m um triangulo do tipo \033[1;32mEQUILÁTERO\033[m')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('As 3 retas \033[1;32mFORMAM\033[m um triangulo \033[1;32mISÓSCELES\033[m')
    else:
        print('As 3 retas \033[1;32mFORMAM\033[m um triangulo \033[1;32mESCALENO\033[m')
else:
    print('As 3 retas \033[1;31mNÃO FORMAM\033[m um triangulo!')
