print('Digite 999 para parar.')
n1 = 0
num_d = 0
soma = 0
pool = ''
while n1 != 999:
    n1 = int(input('Digite um número: \n'))
    if n1 != 999:
        soma += n1
        num_d += 1
        pool += str(n1) + ' '
    else:
        print('Número de parada digitado!')
print('A soma dos {} números digitados foi de {}'.format(num_d, soma))
print('\nCalculo:\n{}\n{}'.format(' + '.join(pool.split()), soma))
