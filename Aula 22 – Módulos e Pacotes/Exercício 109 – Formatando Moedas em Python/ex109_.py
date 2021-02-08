"""Modifique as funções que foram criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o
valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no ex108."""
from moedaF2 import aumentar, dobro, metade, diminuir, moeda
#  import moeda... É a maneira mais recomendada de se importar, pois, pode haver conflitos!

valor = float(input('Digite o preço: R$ '))
print(f'A metade de {moeda(valor)} é {metade(valor)}')
print(f'O dobro de {moeda(valor)} é R$ {dobro(valor)}')
print(f'Aumentando 10% de {moeda(valor)}, temos {aumentar(valor, 10)}')
print(f'Reduzindo 13% de {moeda(valor)}, temos {diminuir(valor, 13)}')
