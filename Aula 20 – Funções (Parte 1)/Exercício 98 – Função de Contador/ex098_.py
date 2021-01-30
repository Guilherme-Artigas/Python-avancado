"""Faça um programa que tenha uma função chamada contador(). que receba três parâmetros. inicio, fim, passo e realize a
contagem. Seu programa tem que realizrar três contagens através da função criada:
A) de 1 até 10, de 1 em 1.
B) de 10 até 0, de 2 em 2.
C) Uma contagem Personalizada."""
from time import sleep


def linha():
    print('+-' * 20)


def contador(p1, p2, p3):
    if p1 < p2:
        if p3 == 0:
            p3 = 1
        print(f'Contagem de {p1} até {p2} de {p3} em {p3}...')
        for indice in range(p1, p2, p3):
            sleep(0.5)
            print(indice, end=' ')
        print()
    if p1 > p2:
        if p3 == 1 or p3 == 0:
            p3 = -1
        elif p3 > 1:
            p3 = -(p3 * 2) + p3
        print(f'Contagem de {p1} até {p2} de {p3} em {p3}...')
        for indice in range(p1, p2 - 1, p3):
            sleep(0.5)
            print(indice, end=' ')
        print('Fim!')


linha()
print('Contagem de 1 até 10 de 1 em 1...')
for indice in range(1, 10):
    sleep(0.5)
    print(indice, end=' ')
print('FIM!')
linha()
print('Contagem de 10 ate 0 de 2 em 2...')
for indice in range(10, -1, -2):
    sleep(0.5)
    print(indice, end=' ')
print('FIM!')
linha()
print('Agora é a sua vez de personalizar a contagem!')
inicio = int(input(f'{"Inicio: ":7}'))
fim = int(input(f'{"Fim":8}'))
passo = int(input(f'{"Passo":8}'))
linha()
contador(inicio, fim, passo)
linha()
