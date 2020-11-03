#Stylos: 0 = none/ 1 = bold/ 4= underline/ 7 = Negative

#Text(cores): /30 = branco /31 = vermelho /32 = verde /33 = laranja/ 34 = azul
#35 = roxo/ 36 = ciano/ 37 = cinza

#Background: Mesma coisa, só começa com 4

#FORMULA \033[STYLE;TEXT;BACKm

print('\033[0;30;41mOlá, Mundo!\033[m')
print('\033[1;33;46mOlá, Mundo!\033[m')
print('\033[1;35;43mOlá, Mundo!\033[m')
print('\033[30;42mOlá, Mundo!\033[m')
print('\033[7;30mOlá, Mundo!\033[m')
print('\033[1;7;40mOlá, Mundo!\033[m')
print('Olá, Mundo!')
#\033[1;30;107m = preto e branco
#\033[1;32m = verde
#\033[1;31m = vermelho
#\033[1;33;107m