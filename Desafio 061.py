a1 = int(input('Digite o primeiro termo da P.A\n'))
r = int(input('Digite a razão da P.A\n'))
PA = a1
conta = 1
string = str(PA)
while conta != 10:
    PA += r
    conta += 1
    string += ' → ' + str(PA)
print(string)