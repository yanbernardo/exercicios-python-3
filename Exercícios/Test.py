##############EXPLICAÇÃO##############
filme = {
    'titulo':'Star Wars',
    'ano':1977,
    'diretor':'George Lucas'
}
print(filme.keys())
print(filme.values())
print(filme.items())
for k, v in filme.items():
    print(f'O {k} é {v}')
locadora = list()
locadora.append(filme)
print(locadora[0]['ano'])
print(locadora[0]['titulo'])
print('=+-'*25,'\n\n')
#############################################
pessoas = {'nome':'Gustavo', 'sexo':'M', 'idade':22}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
del pessoas['sexo']
for k, v in pessoas.items():
    print(f'{k} = {v}')
