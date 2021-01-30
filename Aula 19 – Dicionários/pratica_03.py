# brasil = []
# estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
# estado2 = {'uf': 'Paraná', 'sigla': 'PR'}
# brasil.append(estado1)
# brasil.append(estado2)

# print(estado1)
# print(estado2)
# print(brasil)
# print(brasil[0])
# print(brasil[1])
# print(brasil[0]['uf']) = Rio de Janeiro
# print(brasil[1]['sigla']) = PR
# --------------------------------------------------------------------------------------
estadoDIC = dict()
brasil = list()
for indice in range(0, 3):
    estadoDIC['uf'] = str(input('Unidade Federativa: '))
    estadoDIC['sigla'] = str(input('Sigla do estado: '))
#   Jogando dados de dicionários dentro de lista:
#   brasil.append(estado) -> ERRADO
    brasil.append(estadoDIC.copy())  # CORRETO
"""for estado in brasil:
    for chave in estado.keys():
        print(chave)"""
"""for estado in brasil:
    for valor in estado.values():
        print(f'{valor:20}', end=' ')
    print()"""
"""for estado in brasil:
    for chave, valor in estado.items():
        print(f'O campo {chave} tem valor {valor}')"""


