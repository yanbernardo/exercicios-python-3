classificacao = ('Vasco da Gama', 'Coritiba', 'Fluminense', 'Sport Recife',
                 'Flamengo', 'Botafogo', 'Corinthians', 'Atletico-MG', 'Internacional',
                 'São Paulo', 'Goiás', 'Ceará SC', 'Fortaleza',
                 'Athletico-PR', 'Grêmio', 'Bahia', 'Palmeiras',
                 'Atletico-GO', 'Santos', 'Bragantino-SP')
print('\033[1;30;107mOs primeiros 5 colocados são \033[m\n{}\n'.format('\n'.join(classificacao[:5])))
print('\033[1;30;107mOs ultimos 4 colocados da tabela são\033[m \n{}\n'.format('\n'.join(classificacao[-4:])))
print('\033[1;30;107mTimes em ordem alfabetica\033[m \n{}\n'.format('\n'.join(sorted(classificacao))))
print('\033[1;30;107mO Fluminense está na {}ª posição\033[m'.format(classificacao.index('Fluminense') + 1))