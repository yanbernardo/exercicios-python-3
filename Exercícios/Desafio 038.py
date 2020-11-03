print('\033[34m-=\033[m'* 20)
print('Comparador numérico')
print('\033[34m-=\033[m'* 20)
n1 = float(input('Digite o primeiro número.\n'))
n2 = float(input('Digite o segundo número.\n'))
if n1 > n2:
    print('O \033[4;32mPRIMEIRO\033[m valor digitado é \033[4;35mMAIOR\033[m')
elif n2 > n1:
    print('O \033[4;32mSEGUNDO\033[m valor digitado é \033[4;35mMAIOR\033[m')
else:
    print('\033[4;32mNÃO EXISTE\033[m valor maior, os dois são \033[4;35mIGUAIS\033[m!!')