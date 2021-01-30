""""
Crie uma tupla preenchida com os 20 primeiros colocados da tabela do campeonato brasileiro de futebol.
na ordem de colocação. Depois mostre:

A) Apenas os 5 primeiros colocados.
B) Os últimos 4 colocados da tabela.
C) Uma lista com os times em ordem alfabética.
D) Em que posição da tabela esta o time do Corinthians.
"""
tabela_brasileiro = ('São paulo', 'Atlético-MG', 'Flamengo', 'Internacional', 'Grêmio', 'Palmeiras', 'Fluminense', 'Santos', 'Corinthians', 'Ceará SC', 'Athletico-PR', 'Atlético-GO', 'Bragantino', 'Fortaleza', 'Sport Recife', 'Bahia', 'Vasco da Gama', 'Goiás', 'Botafogo', 'Coritiba')

# Minha solução
"""
print('A - Mostrar apenas os 5 primeiros colocados da tabela.')
print('B - Mostrar apenas os 4 últimos colocados da tabela.')
print('C - Mostrar uma lista com os nome dos times organizados por ordem alfabética.')
print('D - Mostrar em qual posição da tabela encontra-se o Corinthians.')

controle = True
while controle == True:
    opcao = str(input('Digite uma opção: ')).strip().upper()[0]
    if opcao == 'A':
        print(f'Os 5 primeiros colocados do campeonato no momento são: {tabela_brasileiro[:5]}')
        controle = False
    elif opcao == 'B':
        print(f'Os 4 últimos colocados do campeonato no momento são: {tabela_brasileiro[-4:]}')
        controle = False
    elif opcao == 'C':
        print('Times organizados em ordem alfabética é: ')
        print(sorted(tabela_brasileiro))
        controle = False
    elif opcao == 'D':
        for c in range(0, len(tabela_brasileiro)):
            if tabela_brasileiro[c] == 'Corinthians':
                print(f'O Corinthians encontra-se em {c+1}º lugar neste momento do campeonato.')
        controle = False
    else:
        print(f'Você digitou uma opção invalida!')
        controle = True
        print()
"""

# Solução mostrada na aula

print('-=' * 30)
print(f'Lista de times do Brasileirão: {tabela_brasileiro}')
print('-=' * 30)
print(f'Os 5 primeiros são: {tabela_brasileiro[:5]}')
print('-=' * 30)
print(f'Os 4 últimos são: {tabela_brasileiro[-4:]}')
print('-=' * 30)
print(f'Times em ordem alfabética: {sorted(tabela_brasileiro)}')
print('-=' * 30)
print(f'O Corinthians esta na {tabela_brasileiro.index("Corinthians")+1}º posição.')
