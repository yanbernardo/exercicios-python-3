f = str(input('Digite uma frase\n'))
fs = f.title().strip()
f = f.upper().strip().split()
f = ''.join(f)
if f == (f)[:: - 1]:
    print('{} é um PALINDROMO'.format(fs))
else:
    print('{} NÃO é um PALINDROMO'.format(fs))
