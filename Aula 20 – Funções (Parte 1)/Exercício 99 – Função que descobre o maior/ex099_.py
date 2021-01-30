"""Faça um programa que tenha uma função chamada maior(), que receba vários valores com parâmetros com valores valores
inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior."""


def maior(* p1):
    indice = maior = 0
    print('\nAnalisando os valores passados... ')
    for valor in p1:
        if indice == 0 or valor > maior:
            maior = valor
        indice += 1
        print(f'{valor}', end=' ')
    print(f'\nMaior valor foi: {maior}')


# Maior valor
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(2, 1)
maior(6)
maior()
