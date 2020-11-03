lista = list()
more_n = 'S'
while more_n == 'S':
    n = int(input('Digite um valor: '))
    if n not in lista:
        lista.append(n)
        print('Valor adicionado com sucesso.')
    else:
        print('Valor duplicado! Não vou adicionar.')
    more_n = input('Dejesa continuar? (S/N): ').upper()[0]
lista.sort()
print(f'Os valores adicionados em ordem crescente foram: {lista}')