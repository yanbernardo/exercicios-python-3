a1 = int(input('Digite o primeiro termo da P.A\n'))
r = int(input('Digite a razão da P.A\n'))
dnv = 1
PA = a1
stop = 1
conta = 10
string = str(PA)
while conta > 1:
    PA += r
    conta += -1
    string += '|' + str(PA)
print(string)
conta = 1
while stop != 0:
    string = ''
    conta = stop = int(input('Deseja ver mais quantos termos?\n'))
    while conta > 0:
        PA += r
        conta += -1
        string += '|' + str(PA)
    print(string)
