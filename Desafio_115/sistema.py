from Desafio_115.lib.interface import *
from time import sleep
from Desafio_115.lib.arquivo import *

arq = 'cadastros.txt'

if not arqExiste(arq):
    print(f'Arquivo {arq} não foi encontrado')
    createArq(arq)

while True:
    option = menu(['\033[1;34mVer pessoas cadastradas\033[m', '\033[1;34mCadastrar nova Pessoa\033[m', '\033[1;34mSair do Sistema\033[m'])
    if option == 1:
        lerArq(arq)
    elif option == 2:
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: ')).title().strip()
        idade = leiaInt('Idade: ')
        cadPes(arq, nome, idade)
    elif option == 3:
        cabecalho('SAINDO DO SISTEMA... ATÉ LOGO!')
        sleep(1)
        break
    else:
        print('\033[31mERRO! Digite uma opção válida...\033[m')
    sleep(1)
