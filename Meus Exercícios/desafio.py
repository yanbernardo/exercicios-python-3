lista = list()
spc = 0
while True:
    try:
        n = int(input("Digite um número impar: "))
        if n % 2 == 0 or n < 0:
            print('Por favor, digite somente números impares e positivos.')
        else:
            break
    except:
        print('O valor inserido não é um número')
for c in range(1, n+1):
    lista.append(c)
while len(lista) >= 3:
    for num in lista:
        print(num, end=" ")
    print()    
    spc += 2
    print(" "*spc, end="")
    del lista[-1]
    del lista[0]
    if len(lista) == 1:
        print(lista[0])
        break
    