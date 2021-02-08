"""Crie um módulo chamado moeda.py que tenha as funções incorporadas aumetar(), diminuir(), dobro() e metado().
Faça também um programa que importe esse módulo e use algumas dessas funções."""
from moeda import aumentar, dobro, metade, diminuir
#  import moeda... É a maneira mais recomendada de se importar, pois, pode haver conflitos!

valor = float(input('Digite o preço: R$ '))
print(f'A metade de {valor} é {metade(valor)}')
print(f'O dobro de {valor} é {dobro(valor)}')
print(f'Aumentando 10% de {valor}, temos {aumentar(valor, 10)}')
print(f'Reduzindo 13% de {valor}, temos {diminuir(valor, 13)}')
