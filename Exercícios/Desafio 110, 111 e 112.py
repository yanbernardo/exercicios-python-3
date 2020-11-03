from Módulos.uteis import moeda
from Módulos.uteis import dados
n = dados.leiaDinheiro('Digite o preço: R$')
moeda.resumo(n, 80, 35)