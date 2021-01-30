"""lista = []
lista.append('Guilherme')
lista.append(28)
#print(lista)
lista2 = []
lista2.append(lista[:])
lista[0] = 'Bryan'
lista[1] = 6
lista2.append(lista[:])
print(lista2)
"""
"""lista = [['João', 61], ['Guilherme', 28], ['Julia', 1], ['Bryan', 6]]
#       [ [ 0 ],[ 1]],   [   0   ],  [1],  [  0 ], [1],  [  0 ], [1]
#Posição[     0     ], [       1       ], [     2    ], [      3    ]"""
"""for indice in lista:
    print(f'{indice[0]} tem {indice[1]} anos.')"""

lista1 = []
lista2 = []
for controle in range(0, 3):
    lista2.append(str(input('Nome: ')))
    lista2.append(int(input('Idade: ')))
    lista1.append(lista2[:])
    lista2.clear()
for posicao in lista1:
    if posicao[1] >= 21:
        print(f'{posicao[0]} é maior e tem {posicao[1]} anos.')
    else:
        print(f'{posicao[0]} é menor e tem {posicao[1]} anos.')
