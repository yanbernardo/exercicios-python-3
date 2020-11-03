s = str(input('\033[1;30;107mEscolha o sexo(M/F):\033[m ')).upper().strip()[0]
while s not in 'MF':
    print('\033[1;31;107mOPÇÃO INVÁLIDA\033[m\n\033[1;31;107mTENTE NOVAMENTE!\033[m')
    s = str(input('\033[1;30;107mEscolha o sexo(M/F):\033[m ')).upper()[0]
print('\033[1;32;107mINFORMAÇÃO REGISTRADA\033[m')
