nome = str(input('Digite seu nome completo:\n')).strip().title()
print('Seu nome completo é:\n{}\n'.format(nome))
print('Seu primeiro nome é:\n{}\n'.format(nome.split()[0]))
pal = len(nome.split()) - 1
print('Seu ultimo nome é:\n{}\n'.format(nome.split()[pal]))
