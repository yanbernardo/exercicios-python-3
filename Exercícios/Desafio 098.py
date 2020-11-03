from time import sleep
def contador(ini, fim, passo):
    print(f'Contagem de {ini} até {fim} de {passo} em {passo} iniciada...')
    lin()
    sleep(2)
    if passo == 0:
        passo = 1
    passo = abs(passo)
    if fim <= ini:
        for c in range(ini, fim - 1, -passo):
            print(c, end=' ')
            sleep(1)
    else:
        for c in range(ini, fim + 1, passo):
            print(c, end=' ')
            sleep(1)
    print('Fim.')
    lin()
def lin():
    print('=-' * 30)
lin()
contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é sua vez de fazer sua contagem!')
i = int(input('Início: '))
f = int(input('Fim:    '))
p = int(input('Passo:  '))
contador(i, f, p)

