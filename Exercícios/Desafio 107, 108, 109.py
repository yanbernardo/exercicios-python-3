from Módulos.uteis import moeda
n = int(input('Digite o preço: R$ '))
print(f'Aumentando {moeda.moeda(n)} em 10% temos: {moeda.aumentar(n, 10, True)}')
print(f'Reduzindo {moeda.moeda(n)} em 13% temos: {moeda.diminuir(n, 13, True)}')
print(f'O dobro de {moeda.moeda(n)} é igual a {moeda.dobro(n, True)}')
print(f'A metade de {moeda.moeda(n)} é igual a {moeda.metade(n, True)}')