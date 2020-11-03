n = int(input('Digite um número para saber seu fatorial\n'))
cal = n - 1
fat = n
while cal != 0:
    print('{} x {} = {}'.format(fat, cal, fat * cal))
    fat = fat * cal
    cal += -1
print('O fatorial de {}! é {}'.format(n, fat))