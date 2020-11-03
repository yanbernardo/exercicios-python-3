listanum = []
max = min = 0
for c in range(0, 5):
    listanum.append(int(input('Digite um valor para a posição {}: '.format(c))))
    if c == 0:
        max = min = listanum[c]
    else:
        if listanum[c] > max:
            max = listanum[c]
        if listanum[c] < min:
            min = listanum[c]
print('-='*30)
print(f'Os valores digitados foram:\n{listanum}')
print(f'O maior valor foi {max} nas posições ', end = '')
for i, v in enumerate(listanum):
    if v == max:
        print(f'{i}... ', end = '')
print(f'\nO menor valor foi {min} nas posições ', end = '')
for i, v in enumerate(listanum):
    if v == min:
        print(f'{i}... ', end = '')