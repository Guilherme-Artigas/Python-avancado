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

# Esse código gera erro, pois tuplas são imutaveis, não podem ser alteradas.
"""
tupla = (2, 5, 9, 1)
tupla[2] = 3
print(tupla)
"""

lista = [2, 5, 9, 1]
lista[2] = 3
lista.append(7)  # Adiciona um elemento ao final da lista.
lista.sort()  # Organiza os elementos de forma crescente, ou decrescente com a passagem de parametro (reverse=True)
lista.sort(reverse=True)  # Organiza os elementos de forma decrescente.
lista.insert(0, -5)  # Inserindo valores em uma determinda posição, apontando o parametro antes da virgula.
del lista[0]  # Remove o elemento da lista na posição apontada entre os colchetes.
lista.pop()  # Remove o último elemento da lista, ou um elemento da lista especifico apontando um parametro.
lista.remove(2)  # Remove um elemento especifico da lista.
print(lista)
print(f'Essa lista tem {len(lista)} elementos.')
