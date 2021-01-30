"""Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e
quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será
guardado em um dicionário, incluindo o total de gols feitos durante o campeonato."""
cadastro = dict()
lista_gols = list()
soma = 0
cadastro['nome'] = str(input('Nome do Jogador: '))
quantidade_partidas = int(input(f'Quantas partidas {cadastro["nome"]} jogou: '))
for indice in range(0, quantidade_partidas):
    lista_gols.append(int(input(f'Quantos gols na partida {indice + 1}: ')))
    soma += lista_gols[indice]
cadastro['gols'] = lista_gols
cadastro['total'] = soma
print('+-' * 30)
print(cadastro)
print('+-' * 30)
for chave, valor in cadastro.items():
    print(f'O campo {chave} tem o valor {valor}.')
print('+-' * 30)
print(f'O jogador {cadastro["nome"]} jogou {quantidade_partidas} partidas.')
for indice in range(0, len(lista_gols)):
    print(f'        => Na partida {indice + 1}, fez {lista_gols[indice]} gol(s)')
print(f'Foi um total de {cadastro["total"]} gols.')
