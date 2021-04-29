from random import randint
t='Bem-Vindo ao ACERTE O NÚMERO'
print('~'*len(t))
print(t)
print('~'*len(t))
rnum = randint(1,100)
c = 0
while True:
    unum = int(input('Digite um número entre 1 e 100:\n'))
    c+=1
    if unum < rnum:
        print('Valor incorreto, chute mais \033[1;32malto\033[m!')
    if unum > rnum:
        print('Valor incorreto, chute mais \033[1;31mbaixo\033[m!')
    if unum == rnum:
        print(f'Parabens, você acertou o valor {rnum} em {c} tentativas')
        break
