ret = 'S'
while ret == 's' or ret == 'S':
    city = str(input('Digite o nome da sua cidade:\n').strip())
    city = city.upper()
    city = city.split()
    if 'SANTO' in city[0]:
        print('Sua cidade começa com SANTO')
    else:
        print('Sua cidade NÃO começa com SANTO')
    ret = input('Deseja continuar?(S/N)\n')