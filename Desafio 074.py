from random import randint
num = (randint(0, 10), randint(0, 10), randint(0, 10),
       randint(0, 10), randint(0, 10))
print(f'Os valores sorteados foram: ', end = '')
for numero in num:
    print(f'{numero} ', end = '')
print(f'\nO maior valor foi: {max(num)}')
print(f'O menor valor foi: {min(num)}')