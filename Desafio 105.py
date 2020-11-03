def notas(* notas, sit=False):
    """
       --> Mostra um dicionário com a quantidade de alunos, a maior nota da turma,
       a menor nota da turma e a média da turma, pode tambem exibir a situação da mesma (opcional)
    :param notas: Média dos alunos da turma (SEM LIMITE DE ALUNOS)
    :param sit: (OPCIONAL) Se a média da turma está boa ou não.
    :return: Dicionário com todas as informações da turma.
    """
    alunos = dict()
    alunos['total'] = len(notas)
    alunos['maior'] = max(notas)
    alunos['menor'] = min(notas)
    alunos['media'] = sum(notas)/len(notas)
    if sit:
        if alunos['media'] >= 7:
            alunos['situação'] = 'BOA'
        elif 5 <= alunos['media']:
            alunos['situação'] = 'RAZOÁVEL'
        elif alunos['media'] < 5:
            alunos['situação'] = 'RUIM'
    return alunos


print(notas(5.5, 2.5, 1.5, sit=True))

