from random import shuffle
a1 = input('Primeiro nome: ')
a2 = input('Segundo nome: ')
a3 = input('Terceiro nome: ')
a4 = input('Quarto nome: ')
list = [a1, a2, a3, a4]
shuffle(list)
print('A ordem do trabalho foi \n {}'.format(list))
