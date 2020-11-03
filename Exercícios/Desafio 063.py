n = int(input('Quantos termos da sequencia de Fibonacci deseja?\n')) - 1
ap = 0
pa = 1
p = 1
a = '0'
while n != 0:
    a += '|' + str(p)
    p = pa + ap
    ap = pa
    pa = p
    n += -1
print(a)