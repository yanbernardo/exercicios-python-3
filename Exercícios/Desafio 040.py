n1 = float(input('Digite a primeira nota\n'))
n2 = float(input('Digite a segunda nota\n'))
if (n1 + n2)/2 >= 7:
    print('Você foi \033[1;32mAPROVADO\033[m!!')
elif 5 <= (n1 + n2)/2 <= 6.9:
    print('Você está de \033[1;33mRECUPERAÇÃO\033[m!!')
else:
    print('Você está \033[1;31mREPROVADO\033[m!')