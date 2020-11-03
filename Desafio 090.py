alunos = dict()
alunos['nome'] = str(input('Nome: ')).capitalize()
alunos['media'] = float(input(f'Média de {alunos["nome"]}: '))
if alunos['media'] >= 7:
    alunos['situação'] = 'Aprovado'
else:
    alunos['situação'] = 'Reprovado'
print(f'Nome: {alunos["nome"]}')
print(f'A média é {alunos["media"]:.1f}')
print(f'O aluno está {alunos["situação"]}')