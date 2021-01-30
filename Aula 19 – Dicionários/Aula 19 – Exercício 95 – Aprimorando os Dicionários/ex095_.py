"""Aprimore o Desafio 093 para que ele funcione com varios jogadores, incluindo um sistema de visualização de detalhes do
aproveitamento de cada jogador."""
time = list()
dicjogador = dict()
partidas = list()
while True:
    dicjogador.clear()
    dicjogador['nome'] = str(input('Nome do Jogador: '))
    totalP = int(input(f'Quantas partidas {dicjogador["nome"]} jogou: '))
    partidas.clear()
    for indice in range(0, totalP):
        partidas.append(int(input(f'  Quantos gols na partida {indice + 1}: ')))
    dicjogador['gols'] = partidas[:]
    dicjogador['total'] = sum(partidas)
    time.append(dicjogador.copy())
    while True:
        r = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
        if r in 'SN':
            break
        print(f'Você digitou uma resposta invalida! {r}... Por Favor digite S ou N...')
    if r == 'N':
        break
print('-' * 40)
print('cod', end='')
for indice in dicjogador.keys():
    print(f' {indice:<13}', end='')
print()
for chave, valor in enumerate(time):
    print(f'{chave:<4}', end='')
    for dado in valor.values():
        print(f'{str(dado):<14}', end='')
    print()
print('*-' * 30)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 é o flag de parada): '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com o código {busca}! Tente de novo')
    else:
        print(f' ---- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]} ----')
        for indice, gols in enumerate(time[busca]['gols']):
            print(f'  No jogo {indice + 1} fez {gols} gols.')
    print('-' * 40)
print(' <<< Volte sempre >>> ')
