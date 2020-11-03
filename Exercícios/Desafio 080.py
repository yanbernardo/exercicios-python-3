lista = []
for c in range(0, 5):
    n = int(input('Digite um número: '))
#Iniciando a lista
    if c == 0:
        lista.append(n)
    elif c == 1:
        if n >= lista[0]:
            lista.append(n)
        else:
            lista.insert(0, n)
#Comparando o Resto
    elif n >= lista[len(lista) - 1]:
        lista.append(n)
    elif n <= lista[0]:
        lista.insert(0, n)
    else:
        for casa, num in enumerate(lista):
            if lista[casa] <= n <= lista[casa+1]:
                lista.insert(casa + 1, n)
                break
print(f'Os números digitados em ordem crescente foram {lista}')
