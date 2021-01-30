"""Faça um programa que tenha uma lista chamda números e duas funções chamadas sorteia() e somapar(). A primeira função
vai sortear 5 números e vai coloca-los dentro de uma lista e a segunda função vai mostrar a soma entre os valores pares
 sorteados pela função anterior."""
from random import randint
from time import sleep

n_sorteados = []


def sorteia():
    for indice in range(0, 5):
        n = randint(1, 10)
        n_sorteados.append(n)
    print(f'Sorteando 5 valores:', end=' ')
    for indice in n_sorteados:
        sleep(0.5)
        print(indice, end=' ')
    print('PRONTO!')


def somapar():
    somaP = 0
    for indice in n_sorteados:
        if indice % 2 == 0:
            somaP += indice
    print(f'Somando os valores pares de {n_sorteados} = {somaP}')


sorteia()
somapar()
