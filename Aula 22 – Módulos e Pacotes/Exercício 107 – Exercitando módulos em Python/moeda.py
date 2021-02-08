"""Crie um módulo chamado moeda.py que tenha as funções incorporadas aumetar(), diminuir(), dobro() e metado().
Faça também um programa que importe esse módulo e use algumas dessas funções."""


def aumentar(p1, p2):
    res = p1 + (p1 * p2 / 100)
    return res


def diminuir(p1, p2):
    res = p1 - (p1 * p2 / 100)
    return res


def dobro(p1):
    res = p1 * 2
    return res


def metade(p1):
    res = p1 / 2
    return res
