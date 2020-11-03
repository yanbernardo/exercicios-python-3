grupo = ('cachorro', 'gato', 'papagaio', 'piriquito', 'sapo', 'jabuti', 'elefante', 'Ednaldo Pereira')
for palavra in grupo:
    palavra = palavra.lower()
    vogais = ''
    for letra in range(0, len(palavra)):
        if palavra[letra] == 'a':
            vogais += 'a '
        if palavra[letra] == 'e':
            vogais += 'e '
        if palavra[letra] == 'i':
            vogais += 'i '
        if palavra[letra] == 'o':
            vogais += 'o '
        if palavra[letra] == 'u':
            vogais += 'u '
    print(f'Na palavra {palavra} temos {vogais}')
