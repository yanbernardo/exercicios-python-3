listagem = ('6x Pão', 2,
            'Leite', 3,
            'Lápis', 0.50,
            'Caneta', 2,
            'Apagador', 8,
            'Borracha', 2.50)
print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end = '')
    else:
        print('R${:>5.2f}'.format(listagem[pos]))
print('-' * 40)

