t_idade = 0
velho = 0
m_novas = 0
v_nome = ''
for c in range(0,4):
    nome = str(input('\033[1;30;107mDigite seu nome:\033[m ')).capitalize()
    idade = int(input('\033[1;30;107mSua idade:\033[m '))
    sexo = str(input('\033[1;30;107mSeu sexo(M/F):\033[m ')).upper().strip()
    print('\033[1;30;107m-=\033[m'*30)
    t_idade += + idade
    if sexo[:1] == 'M' and velho < idade:
        velho = idade
        v_nome = nome
    elif sexo[:1] == 'F' and idade < 20:
        m_novas += + 1
print('\n\033[1;30;107mA média da idade do grupo é de {} anos\033[m'.format(t_idade / 4))
if velho != 0:
    print('\n\033[1;32;107m{} \033[1;30;107mé o homem mais velho do grupo com {} anos\033[m'.format(v_nome, velho))
else:
    print('\n\033[1;30;107mNão possuem homens no grupo.\033[m')
if m_novas != 0:
    print('\n\033[1;30;107mExistem {} mulheres abaixo dos 20 anos no grupo\033[m'.format(m_novas))
else:
    print('\n\033[1;30;107mNão existem mulheres abaixo dos 20 anos no grupo\033[m')

