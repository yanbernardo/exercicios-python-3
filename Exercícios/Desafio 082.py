numeros = []
pares = []
impares = []
while True:
    numeros.append(int(input('Digite um número: ')))
    m_n = str(input('Deseja continuar?(S/N): ')).upper()[0]
    if m_n == 'N':
        break
for n in numeros:
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
print('-=' * 30)
print(f'Os número digitados foram {numeros}')
print('Destes números, os valores PARES foram:\n{}'.format(pares))
print('E os valores impares foram:\n{}'.format(impares))
