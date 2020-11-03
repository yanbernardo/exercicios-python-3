print('{:=^40}'.format('Bar Do Zé'))
p = float(input('\033[1;30;107mQual o preço das compras?\033[m\nR$'))
print("""\033[1;30;107mEscolha o método de pagamento\033[m\n
\033[1;94mA VISTA, DINHEIRO OU CHEQUE \033[1;31m(10% de desconto)\033[m: tecle 1
\033[1;94mA VISTA NO CARTÃO \033[1;31m(5% de desconto)\033[m: tecle 2
\033[1;94mEM ATÉ 2X NO CARTÃO \033[1;31m(Sem desconto)\033[m: tecle 3
\033[1;94m3x OU MAIS NO CARTÃO \033[1;31m(20% de juros)\033[m: tecle 4\n""")
escolha = int(input('\033[1;30;107mEscolha a forma de pagamento e pressione ENTER para confimar\033[m\n'))
if escolha == 1:
    c = p * 0.9
    print('\033[1;30;107mValor total a pagar: \033[1;94m R${:.2f}\033[m\n\033[1;30;107mVocê economizou \033[1;32mR${:.2f}\033[m'.format(c, p - c))
elif escolha == 2:
    c = p * 0.95
    print('\033[1;30;107mValor total a pagar: \033[1;94m R${:.2f}\033[m\n\033[1;30;107mVocê economizou \033[1;32mR${:.2f}\033[m'.format(c, p - c))
elif escolha == 3:
    parcelas = int(input('\033[1;30;107mEm quantas vezes deseja parcelar?\033[m\n'))
    valor = p / parcelas
    print('\033[1;30;107mValor total a pagar:\033[1;94m R${:.2f}.\033[m'.format(p))
    print('\033[1;30;107mSão {} parcelas de\033[1;94m R${:.2f}\033[m'.format(parcelas, valor))
elif escolha == 4:
    c = p * 1.2
    parcelas = int(input('\033[1;30;107mEm quantas vezes deseja parcelar?\033[m\n'))
    valor = c / parcelas
    print('\033[1;30;107mSerão {} parcelas de \033[1;94mR${:.2f}\033[m'.format(parcelas, valor))
    print('\033[1;30;107mValor a pagar: \033[1;94mR${:.2f}\033[m\n\033[1;30;107mVocê pagou \033[1;31mR${:.2f} a mais\033[m'.format(c, c - p))