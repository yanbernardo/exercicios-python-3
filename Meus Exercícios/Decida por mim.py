from random import randint
respostas = ('Sim', 'Não', 'Talvez', 'Provavelmente sim', 'Provavelmente não')
while True:
    print(respostas[randint(0, 4)])
    r = str(input('Aperte N e Enter para sair.\n'))
    if r in ['N', 'n']:
        break
