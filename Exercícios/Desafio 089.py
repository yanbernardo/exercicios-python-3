###CRIE UM PROGRAMA QUE LEIA NOME E DUAS NOTAS DE VÁRIOS ALUNOS E GUARDE TUDO EM
# UMA LISTA COMPOSTA. NO FINAL, MOSTRE UM BOLETIM CONTENDO A MÉDIA DE CADA UM E
# PERMITA QUE O USUÁRIO POSSA MOSTRAR AS NOTAS DE CADA ALUNO INDIVIDUALMENTE
sala = []
cont = 0
print('-='* 37)
print(f'{"SISTEMA ESCOLAR":=^74}')
print('-='* 37)
while True:
    sala.append(list())
    sala[cont].append(str(input('Nome: ')).capitalize())
    sala[cont].append(float(input('Primeira Nota: ')))
    sala[cont].append(float(input('Segunda Nota: ')))
    cont += 1
    resp = str(input('Deseja adicionar mais notas?(S/N): ')).upper()[0]
    if resp == 'N':
        break
print('-=' * 37)
print(f'{"BOLETIM":=^74}')
print('-=' * 37)
for aluno in sala:
    media = (aluno[1] + aluno[2]) /2
    print(f'{aluno[0]:<30}                                    {media:.1f}')
print('-=' * 37)
resp = str(input('Deseja exibir um aluno específico?[S/N]: ')).upper()[0]
if resp == 'S':
    while True:
        nome = input('Digite o nome do aluno: ').capitalize()
        print('-=' * 37)
        for aluno in sala:
            if aluno[0] == nome:
                print(f'{"NOME":<30}1ª PROVA    2ª PROVA')
                print(f'{aluno[0]:<30}{aluno[1]:.1f}         {aluno[2]:.1f}')
        print('-=' * 37)
        resp = str(input('Deseja procurar por outro aluno?[S/N]: ')).upper()[0]
        if resp == 'N':
            break
print('Fim de Execução')
