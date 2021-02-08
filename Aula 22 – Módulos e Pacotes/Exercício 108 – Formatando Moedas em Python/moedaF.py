"""Adapte o código do desafio 107, criando uma função adicional chamada moeda() que consiga mostrar os valores como uma
valor monetário formatado."""


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
