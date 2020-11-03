lista = list()
for contagem in range(0, 5):
    lista.append(input('Digite um número entre 0 e 10: '))
b = lista[:]
posmin = posmax = ''
cont = 0
max = min = 0
for c, n in enumerate(lista):
    n = int(n)
    if min == 0:
        min = n
    if n <= min:
        min = n
    if n >= max:
        max = n
print(f'Maior: {max} / Posição: ', end = '')
while str(max) in b:
    c = b.index(str(max))
    print(f'{c + cont}... ', end = '')
    b.remove(str(max))
    cont += 1
b = lista[:]
cont = 0
print(f'\nMenor: {min} / Posição: ', end = '')
while str(min) in b:
    c = b.index(str(min))
    print(f'{c + cont}... ', end = '')
    b.remove(str(min))
    cont += 1
