"""
Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha
separados os valores pares e ímpares. No final mostre os valores pares e ímpares em ordem crescente.
"""
lista = [[], []]
n = 0
for indice in range(0, 7):
    n = int(input(f'Digite o {indice + 1}º valor: '))
    if n % 2 == 0:
        lista[0].append(n)
    elif n % 2 == 1:
        lista[1].append(n)
print()
print('+-' * 35)
lista[0].sort()
lista[1].sort()
print(f'Valores Pares digitados: {lista[0]}')
print(f'Valores Ímpares digitados: {lista[1]}')
