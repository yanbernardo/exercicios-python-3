from math import hypot
co = float(input('Digite o valor do primeiro cateto: '))
ca = float(input('Digite o valor do segundo cateto: '))
print('O valor da hipotenusa entre o cateto {} e o cateto {} é de {:.2f}'.format(co, ca, hypot(co, ca)))
