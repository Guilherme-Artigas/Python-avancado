a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
# .count(8) conta quantas vezes o elemento aparece dentro da tupla.
print(f'Quantas vezes o valor 8 aparece dentro da tupla? {c.count(8)}')

# .index(2) mostra em que posição encontra-se o elemento dentro da tupla.
# .index(2, 1) nós tambem conseguimos passar um segundo parametro para procurarmos apartir daquele ponto em diante.
print(f'Qual a posição do valor 1 dentro da tupla? {c.index(1)}')

""""
A tupla é imutavel, ou seja, não podemos acrescentar, retirar um elemento ou modifica-los.
Mais temos a possibilidade de apagar todos os dados salvos dentro de uma tupla, usando o comando del(nome da tupla)
"""