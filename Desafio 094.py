tot = list()
ind = dict()
idt = media = 0
#Pergunta Recursiva
while True:
    ind.clear()
    ind['nome'] = str(input('Nome: ')).title()
    while True:
        ind['sexo'] = str(input('Sexo[M/F]: ')).capitalize()[0]
        if ind['sexo'] in 'MF':
            break
        print('ERRO, SEXO INVÁLIDO! Digite apenas M ou F.')
    ind['idade'] = int(input('Idade: '))
    idt += ind['idade']
    tot.append(ind.copy())
    while True:
        resp = str(input('Cadastrar novamente?[S/N]: ')).capitalize()[0]
        if resp in 'SN':
            break
        else:
            print('ERRO! Responda apenas com S ou N.')
    if resp in 'N':
        break
print('-='*30)
#Número de pessoas
print(f'Ao todo foram {len(tot)} pessoas cadastradas.')
print('-='*30)
#Media de idade do grupo
media = idt/len(tot)
print(f'A media da idade das {len(tot)} pessoas é {media:.2f}')
print('-='*30)
#Nome das mulheres
print('Mulheres cadastradas: ')
for ind in tot:
    if ind['sexo'] == 'F':
        print(f'{ind["nome"]}')
print('-='*30)
#Idade acima da média
print(f'Pessoas com idade acima da média do grupo: ')
for ind in tot:
    if ind['idade'] >= media:
        print(f'Nome: {ind["nome"]:^10}       Sexo: {ind["sexo"]:^3}     Idade: {ind["idade"]:^2}  ')
print('-='*30)
