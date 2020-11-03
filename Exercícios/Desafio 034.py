sal = float(input('Qual o salário do funcionário?\nR$'))
if sal > 1250:
    sal = sal * 1.10
else:
    sal = sal * 1.15
print('O salário deste funcionário será de R${:.2f}'.format(sal))