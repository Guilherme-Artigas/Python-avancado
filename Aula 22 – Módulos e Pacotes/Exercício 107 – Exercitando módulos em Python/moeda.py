"""Crie um módulo chamado moeda.py que tenha as funções incorporadas aumetar(), diminuir(), dobro() e metado().
Faça também um programa que importe esse módulo e use algumas dessas funções."""


def aumentar(p1, p2=0):
    return ((p1 * p2) / 100) + p1


def diminuir(p1, p2=0):
    return p1 - ((p1 * p2) / 100)


def dobro(p1):
    return p1 * 2


def metade(p1):
    return p1 / 2
