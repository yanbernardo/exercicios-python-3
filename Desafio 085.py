todos = [[], []]
for c in range(0, 7):
    n = int(input(f'Digite o {c + 1}º número: '))
    if n % 2 == 0:
        todos[0].append(n)
    else:
        todos[1].append(n)
todos[0].sort()
todos[1].sort()
print(f'Os valores impares foram {todos[1]}')
print(f'Os valores pares foram {todos[0]}')
