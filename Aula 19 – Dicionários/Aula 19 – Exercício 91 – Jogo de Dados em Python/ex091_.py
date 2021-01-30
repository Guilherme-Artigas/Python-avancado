"""
Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário. No final, coloque
esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
"""
# Minha solução 50% completa
"""from random import randint
rodada = {}
for indice in range(0, 4):
    rodada[f'Jogador{indice + 1}'] = randint(1, 6)
print('Valores Sorteados: ')
for chave, valor in rodada.items():
    print(f'O {chave} tirou {valor}')
print('Ranking dos jogadores: ')"""

# Solução da aula
from random import randint
from time import sleep
from operator import itemgetter
jogo = {'Jogador1': randint(1, 6),
        'Jogador2': randint(1, 6),
        'Jogador3': randint(1, 6),
        'Jogador4': randint(1, 6)}
print('Valores Sorteados:')
for chave, valor in jogo.items():
    print(f'{chave} tirou {valor} no dado.')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('-+' * 30)
print(' == RANKING DE JOGADORES == ')
for indice, valor in enumerate(ranking):
    print(f' - {indice + 1}º lugar: {valor[0]} com {valor[1]}')
    sleep(1)
