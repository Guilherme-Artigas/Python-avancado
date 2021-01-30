"""
Faça um programa que leia nome e peso de várias pessoas. Guardando tudo em uma lista no final mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.
"""
# Minha solução
"""lista = list()
aux = []
while True:
    aux.append(str(input('Nome: ')))
    aux.append(float(input('Peso [KG]: ')))
    lista.append(aux[:])
    aux.clear()
    resposta = str(input('Quer continuar? [S/N]: ')).strip().lower()[0]
    if resposta in 'n':
        break
print()
print('+-' * 25)
print(f'Total de pessoas cadastradas: {len(lista)}')
print(f'Lista de pessoas mais "Pesadinhas":', end=' ')
for indice in lista:
    if indice[1] > 90:
        print(f'[{indice[0]}]', end=' ')
print(f'\nLista de pessoas mais "Leves":', end=' ')
for indice in lista:
    if indice[1] < 80:
        print(f'[{indice[0]}]', end=' ')
"""
# Solução apresentada na aula
aux = []
lista = []
maior = menor = 0
while True:
    aux.append(str(input('Nome: ')))
    aux.append(float(input('Peso [KG]: ')))
    if len(lista) == 0:
        maior = menor = aux[1]
    elif aux[1] > maior:
        maior = aux[1]
    elif aux[1] < menor:
        menor = aux[1]
    lista.append(aux[:])
    aux.clear()
    r = str(input('Quer continuar? [S/N]: '))
    if r in 'Nn':
        break
print('+-' * 30)
print(f'Ao todo, você cadastrou {len(lista)} pessoas.')
print(f'Maior peso foi de {maior}KG... ', end='')
for indice in lista:
    if indice[1] == maior:
        print(f'[{indice[0]}]', end=' ')
print(f'\nMenor peso foi de {menor}KG... ', end='')
for indice in lista:
    if indice[1] == menor:
        print(f'[{indice[0]}]', end=' ')
