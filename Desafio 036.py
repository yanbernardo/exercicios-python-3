print('\033[34m-=\033[m' *13)
print('Aprovador de Impréstimos')
print('\033[34m-=\033[m' *13)
casa = float(input('Digite aqui o valor da residencia desejada\nR$ '))
salario = float(input('Quanto você ganha por mês?\nR$ '))
anos = float(input('Em quantos anos você pretende pagar?\n'))
meses = anos * 12
print('Para financiar uma casa de R$\033[32m{:.2f}\033[m em \033[32m{:.2f}\033[m anos, a prestação será de R$\033[32m{:.2f}\033[m\n'.format(casa, anos, casa/meses))
if casa / meses > salario * 0.3:
    print('Emprestimo \033[4;31mNEGADO\033[m!!!')
elif casa / meses < salario * 0.3:
    print('Emprestimo \033[4;32mAPROVADO\033[m!!!')
