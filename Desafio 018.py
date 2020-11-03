from math import radians, sin, cos, tan
ang = float(input('Digite o um angulo: '))
s = sin(radians(ang))
c = cos(radians(ang))
tg = tan(radians(ang))
print('O angulo {:.2f}, possui seno de {:.2f}, cosseno de {:.2f} e tangente de {:.2f}'.format(ang, s, c, tg))
