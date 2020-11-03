m_n = 'S'
lista = []
while m_n == 'S':
    n = int(input('Digite um número: '))
    lista.append(n)
    m_n = str(input('Deseja continuar?(S/N): ')).upper()[0]
print('-=' * 30)
print(f'Foram digitados {len(lista)} números')
reverso = lista[:]
reverso.sort(reverse=True)
print(f'Os valores em ordem decrescente são {reverso}')
if 5 in lista:
    print(f'Existe o valor 5 na lista na posição {lista.index(5) + 1}.')
else:
    print('Não foi encontrado o número 5 na lista.')
