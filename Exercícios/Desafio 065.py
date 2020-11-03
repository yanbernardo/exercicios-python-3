cont = 'S'
soma = 0
conta = 0
min = 0
max = 0
while cont[0] == 'S':
    n = int(input('\033[1;30;107mDigite um número \033[1;4;31minteiro\033[m\033[1;30;107m:\033[m\n'))
    soma += n
    conta += 1
    if n < min:
        min = n
    elif min == 0:
        min = n
    if n > max:
        max = n
    cont = str(input('\n\033[1;30;107mDeseja continuar inserindo números(\033[1;32mS\033[1;30;107m/\033[1;31;107mN\033[1;30;107m)?\033[m\n')).strip().upper()
print('\n\033[1;30;107mA média dos {} valores digitados é \033[1;32m{} / {} = {:.2f}\033[m'.format(conta, soma, conta, soma/conta))
print('\033[1;30;107mMAIOR NÚMERO DIGITADO:\033[1;32m {}\033[m\n\033[1;30;107mMENOR NÚMERO DIGITADO:\033[1;32m {}\033[m'.format(max, min))
