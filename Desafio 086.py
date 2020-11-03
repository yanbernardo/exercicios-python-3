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
for a in range(0, 3):
    print(matrix[a], end = '')
print()
for a in range(3, 6):
    print(matrix[a], end = '')
print()
for a in range(6, 9):
    print(matrix[a], end = '')