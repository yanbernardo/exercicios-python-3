def fatorial(n, show=False):
    """
    --> Calcula o Fatorial de um número
    :param n: Número a ser calculado
    :param show: (Opcional) Mostar a conta, True or False
    :return: Retorna a fatorial de um número n
    """
    f = 1
    conta = ''
    for m in range(n, 0, -1):
        f *= m
        if show:
            if m != 1:
                conta += f'{m} x '
            else:
                conta += f'1 = {f}'
        else:
            conta = f
    return conta


print(fatorial(5, True))
