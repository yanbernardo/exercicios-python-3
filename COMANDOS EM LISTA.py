lista = ['Arroz', 'Feijão', 'Batata'] #Lista
#Remover elementos
#a = del lista[3]
#print(a)
#b = lista.pop(1)
#print(b)
#c = lista.remove('Feijão')
#print(c)
#---------------------------------
#if 'item' in lista: (pode ser usado)
valores = list(range(4,11))
print(valores)
valores = [9, 2, 6, 4, 6, 5]
#Para ordenar numeros em ordem crescente
valores.sort()
print(valores)
valores.sort(reverse=True)
print(valores)
print(len(valores))
#
num = [2, 5, 9, 0]
print(num)
#
num[2] = 3
print(num)
#
num.append(7)
print(num)
#
num.sort()
print(num)
#
num.sort(reverse=True)
print(num)
#
print(f'Essa lista tem {len(num)} elementos')
#
num.insert(2, 0)
print(num)
#
num.pop(0)
print(num)
#
num.remove(0)
print(num)
#
valores = list()
valores.append(7)
valores.append(5)
valores.append(3)
for c, v in enumerate(valores):
    print(f'Ná posição {c} achei o valor {v}!')