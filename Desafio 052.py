print('-='*15)
print('\033[1;30;107mCALCULADORA DE NÚMEROS PRIMOS\033[m')
print('-='*15)
n = int(input('\033[1;30;107mDigite um número \033[1;32mINTEIRO\033[m:\n'))
conta = n
vezes = 0
for c in range(conta, 0, -1):
    if n % conta == 0:
        vezes += 1
        conta += -1
    else:
        conta += -1
if vezes == 2:
    print('\033[1;30;107mO número {} é \033[1;32;107mPRIMO\033[m'.format(n))
else:
    print('\033[1;30;107mO numero {} \033[1;31;107mNÃO é PRIMO\033[m'.format(n))
