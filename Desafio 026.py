f = str(input('Digite uma frase:\n')).strip().upper()
print('A letra A aparece na sua frase {} vezes\n'.format(f.count('A')))
print('Ela aparece a primeira vez no {}º caractere'.format(f.find('A') + 1))
print('A última letra A apareceu na posição {}'.format(f.rfind('A') + 1))
