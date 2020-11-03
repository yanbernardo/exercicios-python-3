nome = input('Digite seu nome aqui: ')
print('-'*40)
print()
nome = nome.strip()
print('Seu nome com todas as letras maiúsculas:\n{}\n'.format(nome.upper()))
print('Seu nome com todas as letras minúsculas:\n{}\n'.format(nome.lower()))
list = nome.split()
cd = int(len(list)) - 1
conta = 0
while cd >= 0:
    conta = conta + int(len(list[cd]))
    cd = cd - 1
print('O número de caracteres sem contar os espaços é:\n{}\n'.format(conta))
print('O número de letras de seu primeiro ({}) nome é:\n{}\n'.format(list[0], len(list[0])))
