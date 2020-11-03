n1 = int(input('Insira o primeiro número\n'))
n2 = int(input('Insira o segundo número\n'))
if n1 < n2:
    menor = n1
    maior = n2
else:
    menor = n2
    maior = n1
n3 = int(input('Insira o terceiro número\n'))
if n3 < menor:
    menor = n3
if n3 > maior:
    maior = n3
print('Menor = {}\n'.format(menor))
print('Maior = {}\n'.format(maior))
