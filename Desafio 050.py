soma = 0
for c in range(0, 6):
    n1 = int(input('Digite um número\n'))
    if n1 % 2 == 0:
        soma += n1
print('Os valores pares digitados dão a soma de {}'.format(soma))
