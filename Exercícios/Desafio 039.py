from datetime import date
ano = date.today().year
print('\033[7;32;40m-=\033[m'* 18)
print('\033[1mBEM-VINDO AO EXÉRCITO BRASILEIRO\033[m')
print('\033[7;32;40m-=\033[m'* 18)
nasc = int(input('Informe o ano em que você nasceu.\n'))
if ano - nasc == 18:
    print('Está \033[1;32mNA HORA\033[m de se alistar amigão.')
elif ano - nasc > 18:
    print('Você está \033[1;31mATRASADO\033[m em \033[1;31m{}\033[m anos para o alistamento.'.format((ano - nasc) - 18))
else:
    print('Ainda \033[1;32mFALTAM {} ANOS\033[m para o seu alistamento.'.format(18 - (ano - nasc)))

