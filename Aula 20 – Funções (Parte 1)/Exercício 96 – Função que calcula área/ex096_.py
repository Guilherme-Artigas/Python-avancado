"""Faça um programa que tenha uma função chamada área(). Que receba as dimensões de um terreno retangular
(largura e comprimento) e mostre a área do terreno."""


def linha():
    print('-' * 20)


def area(p1, p2):
    a = p1 * p2
    print(f'A área do seu terreno {p1} x {p2} é de {a}m².')


# Programa Principal
print('Controle de terrenos')
linha()
largura = float(input('LARGURA (m): '))
comprim = float(input('Comprimento (m): '))
area(largura, comprim)
