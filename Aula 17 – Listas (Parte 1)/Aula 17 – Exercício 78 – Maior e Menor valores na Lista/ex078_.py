""""
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.

No final, mostre qual foi o maior e o menor valor digitado e suas respectivas posições dentro da lista.
"""
# Minha solução
lista = list()  # lista = [] 2º opção para a mesma declaração.
maior = menor = laco = 0
for indice in range(0, 5):
    laco += 1
    lista.append(int(input(f'Digite o {laco}º valor: ')))
    if laco == 1:
        maior = lista[indice]
        menor = lista[indice]
    elif lista[indice] > maior:
        maior = lista[indice]
    elif lista[indice] < menor:
        menor = lista[indice]
print('=-' * 30)
print(f'Você digitou os valores: {lista}')
print(f'O maior valor digitado foi {maior} nos indices ', end='')
for indice in range(0, len(lista)):
    if lista[indice] == maior:
        print(f'{indice}', end=', ')
print(f'\nO menor valor digitado foi {menor} nos indices ', end='')
for indice in range(0, len(lista)):
    if lista[indice] == menor:
        print(f'{indice}', end=', ')
