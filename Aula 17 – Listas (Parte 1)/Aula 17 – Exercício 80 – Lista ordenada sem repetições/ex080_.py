""""
Crie um programa onde o usuário possa digitar 5 valores numéricos e cadastre-os em uma lista. Já na posição correta
de inserção (sem usar o .sort()).

No final mostre a lista ordenada na tela.
"""
# Minha solução
"""lista = []
for controle in range(0, 5):
    n = int(input((f'Digite o {controle + 1}º valor: ')))
    lista.append(n)
    if controle > 0:
        for indice in range(0, len(lista)):
            for indice2 in range(indice + 1, len(lista)):
                if lista[indice] > lista[indice2]:
                    a1 = lista[indice2]
                    del lista[indice2]
                    lista.insert(indice, a1)
print(f'Lista organizada na ordem = {lista}')
"""
# Solução apresentada na aula
lista = []
for indice in range(0, 5):
    valor = int(input('Digite um valor: '))
    if indice == 0 or valor > lista[-1]:
        lista.append(valor)
        print(f'Adicionado ao final da lista... ')
    else:
        indice2 = 0
        while indice2 < len(lista):
            if valor <= lista[indice2]:
                lista.insert(indice2, valor)
                print(f'Adicionado na posição {indice2} da lista...')
                break
            indice2 += 1
print('*-' * 25)
print(f'Lista de valores digitados em ordem: {lista}')
