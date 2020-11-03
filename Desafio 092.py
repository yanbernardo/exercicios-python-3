from datetime import datetime
ano_atual = datetime.now().year
info_p = dict()
info_p['nome'] = str(input('Nome: ')).capitalize()
ano = int(input('Ano de nascimento: '))
info_p['idade'] = int(ano_atual) - ano
info_p['CTPS'] = int(input('Número da Carteira de trabalho?[0 se não possuir]:\n'))
if info_p['CTPS'] != 0:
    info_p['contratacao'] = int(input('Ano de contratação: '))
    info_p['salario'] = float(input('Salário: R$'))
    ano_cump = ano_atual - info_p['contratacao']
    if ano_cump < 35:
        info_p['Aposentadoria'] = (35 - ano_cump) + info_p['idade']
    else:
        info_p['Aposentadoria'] = 'Já pode se aposentar!'
else:
    info_p['CTPS'] = 'N/A'
print('-='*22)
for dado, info in info_p.items():
    print(f' - O(A) {dado} tem valor de {info}.')
print('-='*22)
