a1 = int(input('Digite o primeiro termo da P.A\n'))
r = int(input('Digite a razão da P.A\n'))
grupo = ''
for c in range(a1, r*10+1, r):
    print('{}'.format(c), end= ' - ')
print(grupo[1:])