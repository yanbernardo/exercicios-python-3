from random import choice
replay = 'S'
while replay == 's' or replay == 'S':
    print('\033[1;30;107m-=\033[m'* 14)
    print('\033[1;30;107m JOGO PEDRA, PAPEL E TESOURA\033[m')
    print('\033[1;30;107m-=\033[m'* 14)
    pool = ['Pedra', 'Papel', 'Tesoura']
    pc = choice(pool)
    player = str(input('\033[1;30;107mEscolha entre Pedra, Papel ou Tesoura\033[m\n')).strip().title()
    print('\033[1;30;107mA maquina escolheu {}\033[m'.format(pc))
#Possibilidades de VITÓRIA do Jogador
    if pc == 'Pedra' and player == 'Papel' or pc == 'Tesoura' and player == 'Pedra' or pc == 'Papel' and player == 'Tesoura':
        print('\033[1;30;107mVocê \033[1;32;107mGANHOU\033[m!\n\033[1;32;107mPARABÉNS\033[m!!')
#Possibilidades de DERROTA do Jogador
    elif pc == 'Pedra' and player == 'Tesoura' or pc == 'Tesoura' and player == 'Papel' or pc == 'Papel' and player == 'Pedra':
        print('\033[1;30;107mVoce \033[1;31mPERDEU\033[m\n\033[1;30;107mMais sorte na próxima :/\033[m')
#Possibilidade de EMPATE do Jogador
    elif pc == player:
        print('\033[1;33;107mEMPATE\033[1;30;107m!!\033[m')
        print('\033[1;30;107mVocê jogou bem!!\033[m')
    print('\033[1;30;107m-=\033[m' * 14)
    print('\033[1;30;107mDeseja tentar novamente?(S/N)\033[m')
    replay = input('\033[1;30;107m-=\033[m'*14+'\n')
