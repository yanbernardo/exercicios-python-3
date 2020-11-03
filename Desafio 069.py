c_idade = n_homens =  n_mulheresu20 = quant = 0
idade = None
while True:
    keep = ''
    sexo = ''
    quant += 1
    print('-='*20)
    print(f'{quant}ª Pessoa Cadastrada')
    print('-=' * 20)
    while True:
        try:
            idade = int(input('Sua idade:\n'))
            break
        except ValueError:
            print('Número inteiro, por favor!')
    while sexo != 'F' and sexo != 'M':
        sexo = str(input('Sexo[M/F]:\n')).upper()[0]
        if sexo == 'F':
            print('Sexo Feminino cadastrado')
        if sexo == 'M':
            print('Sexo Masculino cadastrado')
    if idade > 18:
        c_idade += 1
    if sexo == 'M':
        n_homens += 1
    if sexo == 'F' and idade < 20:
        n_mulheresu20 += 1
    while keep != 'S' and keep != 'N':
        keep = input('Deseja continuar?[S/N]\n').upper()[0]
    if keep == 'N':
        break
print(f'De {quant} pessoas cadastradas {c_idade} tem mais de 18 anos')
print(f'Ao todo, foram {n_homens} homens cadastrados')
print(f'Foram contabilizadas {n_mulheresu20} mulheres abaixo dos 20 anos')