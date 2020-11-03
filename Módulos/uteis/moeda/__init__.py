def aumentar(value, percent, moeda=False):
    value = value + (value * (percent/100))
    if moeda:
        return f'RS{value:.2f}'
    else:
        return value


def diminuir(value, percent, moeda=False):
    value = value - (value * (percent/100))
    if moeda:
        return f'RS{value:.2f}'
    else:
        return value


def dobro(value, moeda=False):
    value *= 2
    if moeda:
        return f'RS{value:.2f}'
    else:
        return value


def metade(value, moeda=False):
    value = value / 2
    if moeda:
        return f'RS{value:.2f}'
    else:
        return value


def moeda(v):
    return f'RS{v:.2f}'


def titulo(t):
    print('-' * (len(t) + 14))
    print(f'       {t}')
    print('-' * (len(t) + 14))


def resumo(value, a, d):
    titulo('RESUMO DO VALOR')
    price = f'R${value:.2f}'
    print(f'Preço analisado:   {str(price).replace(".", ",")}')
    print(f'Dobro do preço:    {str(dobro(value, True)).replace(".", ",")}')
    print(f'Metade do preço:   {str(metade(value, True)).replace(".", ",")}')
    print(f'80% de aumento:    {str(aumentar(value, a, True)).replace(".", ",")}')
    print(f'35% de redução:    {str(diminuir(value, d, True)).replace(".", ",")}')
