t_preco = c_count = min = 0
while True:
    ex = ''
    p_nome = str(input('Qual é o produto?\n')).capitalize()
    p_preco = float(input('Qual o preço do produto?\nR$'))
    t_preco += p_preco
    if p_preco > 1000:
        c_count += 1
    if min == 0:
        min = p_preco
        b_nome = p_nome
    if p_preco < min:
        min = p_preco
        b_nome = p_nome
    while ex != 'S' and ex != 'N':
        ex = str(input('Deseja Colocar mais produtos?[S/N]\n')).upper()[0]
    if ex == 'N':
        break
print(f'O total gasto na compra foi de R$\033[1;32m{t_preco:.2f}\033[m')
print(f'{c_count} produtos custam mais que R$1000.00')
print(f'O produto mais barato da lista foi \033[1;32m{b_nome}\033[m custando R${min:.2f}')