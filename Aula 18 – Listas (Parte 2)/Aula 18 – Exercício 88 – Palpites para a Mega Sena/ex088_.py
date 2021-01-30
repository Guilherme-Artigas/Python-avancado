"""
Faça um programa que ajude um jogador da Mega-Sena a cria palpites. O programa vai perguntar quantos jogos serão gerados
e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
"""
from time import sleep
from random import randint
aux = []
lista = []
print('+-' * 15)
print(f'{"PALPITROMETRO DA MEGA":^30}')
print('+-' * 15)
limite = int(input('Quantos palpites você precisa: '))
print()
print('-+' * 5, f'SORTEANDO {limite} JOGOS', '-+' * 5)
for controle in range(0, limite):
    aux = [randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60)]
    for indice in range(0, len(aux)):
        for indice2 in range(indice + 1, len(aux)):
            if aux[indice] == aux[indice2]:
                aux[indice2] = randint(1, 60)
    aux.sort()
    lista.append(aux[:])
for controle in range(0, limite):
    print(f'Jogo {controle + 1}: {lista[controle]}')
    sleep(2)
