"""Faça um programa que tenha uma função chamada escreva(). Que receba um texto qualquer como parâmetro e mostre uma
mensagem com tamanho adaptável.
Ex: escreva('olá, Mundo!')
Saida:
~~~~~~~~~~
Olá,Mundo!
~~~~~~~~~~"""


# Minha solução
"""def escreva(p1):
    indice = 0
    while indice < len(p1):
        print('-', end='')
        indice += 1
    print()
    print(p1)
    indice = 0
    while indice < len(p1):
        print('-', end='')
        indice += 1


# Programa Principal
escreva(' * Centro de Treinamento Monte Horebe * ')
"""

# Solução apresentada na aula


def escreva(p1):
    tam = len(p1) + 4
    print('~' * tam)
    print(f'  {p1}')
    print('~' * tam)


escreva('Guilherme Artigas')
escreva('Curso de Phyton Youtube')
