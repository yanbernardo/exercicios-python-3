def escreva(x):
    print('~' * (len(x) + 6))
    print(f'   {x}   ')
    print('~' * (len(x) + 6))


while True:
    frase = str(input('Digite uma frase para o cabeçalho:\n'))
    escreva(frase)
    r = str(input('Digite N para parar: '))
    if r in 'nN':
        break
