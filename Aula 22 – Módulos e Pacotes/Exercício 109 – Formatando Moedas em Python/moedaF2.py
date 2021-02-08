"""Modifique as funções que foram criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o
valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no ex108."""


def aumentar(p1, p2=0):
    return f'R$ {((p1 * p2) / 100) + p1:.2f}'


def diminuir(p1, p2=0):
    return f'R$ {p1 - ((p1 * p2) / 100):.2f}'


def dobro(p1):
    return f'R$ {p1 * 2:.2f}'


def metade(p1):
    return f'R$ {p1 / 2:.2f}'


def moeda(p1):
    return f'R$ {p1:.2f}'
