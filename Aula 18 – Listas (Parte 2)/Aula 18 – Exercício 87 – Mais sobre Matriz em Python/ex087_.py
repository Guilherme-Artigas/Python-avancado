"""
Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.
"""
matriz = []
somaP = somaT = 0
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz.append(int(input(f'[{linha}, {coluna}]: ')))
print()
print('+-' * 15)
for indice, valor in enumerate(matriz):
    if indice == 2 or indice == 5 or indice == 8:
        somaT += valor
        print()
    if valor % 2 == 0:
        somaP += valor
    if indice == 3 or indice == 4 and valor > maior or indice == 5 and valor > maior:
        maior = valor
print()
print(f'Soma dos valores Pares digitados: {somaP}')
print(f'A soma dos valores da 3º coluna: {somaT}')
print(f'O maior valor da 2º linha: {maior}')
