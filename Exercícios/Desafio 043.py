print('\033[4;30;107m-=\033[m' * 20)
print('\033[1;94mCALCULADORA DE INDÍCE DE MASSA CORPÓREA\033[m')
print('\033[4;30;107m-=\033[m' * 20)
weight = float(input('Digite seu peso(Kg):\n'))
height =float(input('Digite a sua altura(m):\n'))
IMC = weight / height**2
print('Seu Indice de Massa Corpórea é de \033[1;94m{:.1f}'.format(IMC))
if IMC > 40:
    print('Obesidade MÓRBIDA!!!')
    print('Procure um nutricionista IMEDIATAMENTE.')
elif 30 < IMC <= 40:
    print('Você está OBESO!')
    print('Procure um nutricionista.')
elif 25 < IMC <= 30:
    print('Você está ÁCIMA DO PESO.')
    print('Procure um nutricionista.')
elif 18.5 < IMC <=25:
    print('Você está no PESO IDEAL')
    print('PARABÉNS!!')
elif IMC <= 18.5:
    print('Você está ABAIXO DO PESO')
    print('Procure um nutricionista.')
