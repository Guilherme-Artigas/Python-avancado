"""Adapte o código do desafio 107, criando uma função adicional chamada moeda() que consiga mostrar os valores como uma
valor monetário formatado."""
from moedaF import aumentar, dobro, metade, diminuir, moeda
#  import moeda... É a maneira mais recomendada de se importar, pois, pode haver conflitos!

valor = float(input('Digite o preço: R$ '))
print(f'A metade de {moeda(valor)} é {metade(valor)}')
print(f'O dobro de {moeda(valor)} é R$ {dobro(valor)}')
print(f'Aumentando 10% de {moeda(valor)}, temos {aumentar(valor, 10)}')
print(f'Reduzindo 13% de {moeda(valor)}, temos {diminuir(valor, 13)}')
