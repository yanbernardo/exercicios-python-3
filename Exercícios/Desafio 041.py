from datetime import datetime
ano = datetime.now()
ano = ano.year
id = int(input('Ano de nascimento:\n'))
if (ano - id) > 20:
    print('Nadador pertencente a categoria \033[1;34mMASTER\033[m')
elif (ano - id) == 20:
    print('Nadador pertencente a categoria \033[1;34mSÊNIOR\033[m')
elif 14 < (ano - id) <= 19:
    print('Nadador pertencente a categoria \033[1;34mJUNIOR\033[m')
elif 9 < (ano - id) <= 14:
    print('Nadador pertencente a categoria \033[1;34mINFANTIL\033[m')
elif 5 < (ano - id) <=9:
    print('Nadador pertencente a categoria \033[1;34mMIRIM\033[m')
else:
    print('\033[1;31mNadador muito novo para competir\033[m')