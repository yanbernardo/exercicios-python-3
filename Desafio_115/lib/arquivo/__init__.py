from Desafio_115.lib.interface import *


def arqExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def createArq(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um erro na criação do arquivo')
    else:
        print(f'Arquivo {nome} criado com sucesso')


def lerArq(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo...')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<34}{dado[1]} anos')
    finally:
        a.close()

def cadPes(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at+')
    except:
        print('Não foi possivel abrir o arquivo.')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um erro na hora de escrever os dados.')
        else:
            print(f'Novo cadastro de {nome} realizado!')
            a.close()