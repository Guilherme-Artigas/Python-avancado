""""
Crie um programa que vai ler vários números e colocar em ums lista. Depois disso crie duas listas extras que vão conter
apenas os valores pares, e os valores impares digitados, respectivamente. Ao final mostre o conteúdo das três listas.
"""
lista = []
pares = []
impares = []

controle = True
while controle:
    valor = int(input('Digite um valor: '))
    lista.append(valor)
    if valor % 2 == 0:
        pares.append(valor)
    elif valor % 2 == 1:
        impares.append(valor)
    r = True
    while r:
        r = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
        if r == 'S':
            controle = True
            r = False
        elif r == 'N':
            controle = False
            r = False
        else:
            print('Você digitou uma resposta invalida! por favor tente de novo... ')
            r = True
print('=-' * 25)
print(f'Lista com todos os valores: {lista}')
print(f'Lista com valores pares: {pares}')
print(f'Lista com valores impares: {impares}')
