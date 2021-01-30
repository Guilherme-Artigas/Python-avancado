"""
Crie um programa que cria uuma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. No final mostre a
matriz na tela, com a formatação correta.
"""
matriz = []
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz.append(int(input(f'[{linha}, {coluna}]: ')))
print()
print('+-' * 15)
for indice, valor in enumerate(matriz):
    print(f'[{valor:^5}]', end=' ')
    if indice == 2 or indice == 5:
        print()
