ret = 's'
while ret == 's' or ret == 'S':
    nome = str(input('Digite aqui seu nome completo:\n')).strip()
    nome = nome.upper()
    if 'SILVA' in nome:
        print('Você é só mais um SILVA que a estrela não brilha')
    else:
        print('Ui Ui Ui, o diferentão não é SILVA')
    ret = input('Deseja continuar?(S/N)\n')