matrix = [[], [], [], [], [], [], [], [], []]
linha = 0
coluna = 0
for c in range(0, 9):
    matrix[c].append(int(input(f'Digite um valor para [{linha}, {coluna}]: ')))
    coluna += 1
    if c in [2, 5]:
        linha += 1
    if coluna == 3:
        coluna = 0
print('-=' * 20)
#primeira linha
for a in range(0, 3):
    print(matrix[a], end = '')
print()
#Segunda Linha
for a in range(3, 6):
    print(matrix[a], end = '')
print()
#Terceira Linha
for a in range(6, 9):
    print(matrix[a], end = '')
print()
################################################
print(f'A soma dos números pares é: ', end= '')
par = 0
for lista in matrix:
    for numero in lista:
        if numero % 2 == 0:
            par += numero
print(par)
print(f'A soma dos itens da terceira coluna é igual a: {matrix[2][0] + matrix[5][0] + matrix[8][0]}')
max = 0
for a in range(3, 6):
    if max == 0 or max < matrix[a][0]:
        max = matrix[a][0]
print(f'O maior valor da segunda linha é {max}')
