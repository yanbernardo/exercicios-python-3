pessoa = list()
grupo = list()
ac_peso = list()
ab_peso = list()
tot = 0
while True:
    pessoa.append(str(input('Nome: ')).capitalize())
    pessoa.append(float(input('Peso: ')))
    grupo.append(pessoa[:])
    pessoa.clear()
    tot += 1
    resp = str(input('Deseja continuar?(S/N): ')).upper()[0]
    if resp == 'N':
        break
print('-=' * 30)
print(f'Ao total foram {tot} pessoas cadastradas.')
for pessoa in grupo:
    if pessoa[1] >= 100:
        ac_peso.append(pessoa[0])
    elif pessoa[1] <= 70:
        ab_peso.append(pessoa[0])
if ac_peso == []:
    print('Não existem pessoas acima dos 100 kg!')
else:
    print('As pessoas acima de 100kg são: ', end = '')
    for nome in ac_peso:
        print(f'{nome}... ', end = '')
print('\n')
if ab_peso == []:
    print('Não existem pessoas abaixo de 70kg')
else:
    print('As pessoas abaixo de 70kg são: ', end = '')
    for nome in ab_peso:
        print(f'{nome}... ', end = '')