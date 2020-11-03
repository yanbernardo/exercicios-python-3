par = 0
tupla = (int(input('Digite um valor: ')),
         int(input('Digite outro valor: ')),
         int(input('Digite outro valor: ')),
         int(input('Digite o último valor: ')))
print(f'Você digitou os números: ', end = '')
for num in tupla:
    print(f'{num} ', end = '')
print('\nO valor 9 apareceu {} vezes'.format(tupla.count(9)))
if 3 in tupla:
    print('O primeiro número 3 foi digitado na {}ª posição'.format(tupla.index(3) + 1))
else:
    print('O número 3 não apareceu nenhuma vez')
print('Os valores pares foram:')
for numero in tupla:
    if numero % 2 == 0:
        par += 1
        print(f'{numero} ', end = ' ')
if par == 0:
    print('Não foram encontrados valores pares')



