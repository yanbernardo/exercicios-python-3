from random import randint
from time import sleep


def sorteia(lista):
    print(f'Sorteando os valores da lista:', end=' ')
    for c in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(n, end=' ')
        sleep(0.4)
    print()


def somaPar(lista):
    soma = 0
    for n in lista:
        if n % 2 == 0:
            soma += n
    print(f'A soma dos valores pares da lista é igual a {soma}!')


numeros = list()
sorteia(numeros)
somaPar(numeros)
