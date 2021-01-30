""""
lanche.append('cookie')  adiciona um elemento ao final da lista.
lanche.insert(0, 'cachorro quente')  .insert() adiciona elementos a lista em qualquer posição.

Temos 3 formas de apagar itens em listas:
del lanche[3]
lanche.pop(3)  normalmente o pop elimina o ultimo item da lista, mais temos como passar o parametro, apontando qual posição sera excluida
lanche.remove('pizza') excluindo item pelo nome/valor

Todos esses comandos eliminam o item/indice e faz uma reposição da lista de forma automatica.

if 'pizza' in lanche:
    lanche.remove('pizza')

valores = list(range(4, 11))

    valores
    4, 5, 6, 7, 8, 9, 10 - Valores da lista com nome de valores.
    0, 1, 2, 3, 4, 5, 6 - indices da lista.

valores = [8, 2, 5, 4, 9, 3, 0]
valores.sort() .sort() organiza as lista de forma crescente.
    valores
    [0, 2, 3, 4, 5, 8, 9]

valores.sort(reverse=True) temos como fazer a passagem de parametro (reverse=True), para que a lista seja organizada de forma decrescente.
    valores
    [9, 8, 5, 4, 3, 2, 0]

len(valores) len() retorna quantos elementos tem dentro da lista.
>> 7
"""

lista = []
lista.append(5)
lista.append(9)
lista.append(4)

"""for valor in lista:  # Para cada valor na lista, mostre!
    print(f'{valor} ... ', end='')"""

"""for indice, valor in enumerate(lista):
    print(f'Indice: {indice} -> Valor: {valor}')"""

"""for valor in range(1, 6):
    lista.append(int(input(f'Digite o {valor}º valor: ')))
print(lista)"""

"""a = [2, 3, 4, 7]
b = a  # Essa atribuição faz uma ligação entre elas, ou seja, qualquer alteração afeta as duas.
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')"""

"""a = [2, 3, 4, 7]
b = a[:]  # Essa atribuição faz uma cópia de todos os valores de a para b, dessa forma podemos altera-las de forma independente.
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')"""
