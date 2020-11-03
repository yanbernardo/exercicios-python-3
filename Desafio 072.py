while True:
    stop = ''
    n = int(input('Digite um número entre 0 e 20: '))
    n_extenso = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis',
                 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze',
                 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito',
                 'Dezenove' , 'Vinte')
    while n < 0 or n > 20:
        n = int(input('Tente novamente! Digite um número entre 0 e 20: '))
    print(f'Você digitou o número \033[4;32m{n_extenso[n]}\033[m')
    while stop != 'S' and stop != 'N':
        try:
            stop = str(input('Deseja continuar?[S/N] ')).upper().strip()[0]
        except:
            print('Você não digitou nada, ', end = '')
    if stop == 'N':
        print('Fim de Execução')
        break
