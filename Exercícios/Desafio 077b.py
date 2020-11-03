grupo = ('mercado', 'cachorro', 'gato', 'papagaio', 'piriquito', 'sapo', 'jabuti', 'elefante', 'Ednaldo Pereira')
for palavra in grupo:
    palavra = palavra.lower()
    print(f'\nNa palavra {palavra}, temos ', end = '')
    for letra in palavra:
        if letra in 'aeiou':
            print(letra, end = ' ')