from time import sleep
def maior(* num):
    max = 0
    for n in num:
        print(n, end=' ')
        sleep(0.4)
        if max == 0:
            max = n
        if max < n:
            max = n
    print(f'\nForam informados {len(num)} valores ao todo.')
    sleep(0.4)
    print(f'O maior valor informado foi {max}!')
def lin():
    print('-=' * 30)

lin()
maior(7, 3, 9, 0, 12, 5)
lin()
maior(2, 9, 4, 5, 7, 1)
lin()
maior(4, 7, 0)
lin()
maior(1, 2)
lin()
maior(6)
lin()
maior()
lin()





