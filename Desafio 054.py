from datetime import date
ano = date.today().year
maior = 0
menor = 0
for c in range(0, 7):
    n1 = int(input('Digite aqui o {}º ano de nascimento\n'.format(c + 1)))
    if ano - n1 >= 21:
        maior += + 1
    else:
        menor += +1
print('{} pessoas já são maior de idade e {} ainda são menores'.format(maior, menor))