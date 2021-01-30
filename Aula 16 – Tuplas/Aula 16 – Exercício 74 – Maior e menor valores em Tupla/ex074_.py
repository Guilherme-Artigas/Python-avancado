""""
Crie um programa que vai gerar cinco numeros aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
"""
# Minha solução
"""
from random import randint

v1 = randint(1, 10)
v2 = randint(1, 10)
v3 = randint(1, 10)
v4 = randint(1, 10)
v5 = randint(1, 10)

tupla = (v1, v2, v3, v4, v5)

print(f'Valores sorteados foram: {tupla}')

if v1 >= v2 and v1 >= v3 and v1 >= v4 and v1 >= v5:
    maior = v1
    menor = v1
else:
    menor = v1

if v2 >= v1 and v2 >= v3 and v2 >= v4 and v2 >= v5:
    maior = v2
elif v2 < menor:
    menor = v2

if v3 >= v1 and v3 >= v2 and v3 >= v4 and v3 >= v5:
    maior = v3
elif v3 < menor:
    menor = v3

if v4 >= v1 and v4 >= v2 and v4 >= v3 and v4 >= v5:
    maior = v4
elif v4 < menor:
    menor = v4

if v5 >= v1 and v5 >= v2 and v5 >= v3 and v5 >= v4:
    maior = v5
elif v5 < menor:
    menor = v5
print(f'Maior valor sorteado foi: {maior}')
print(f'Menor valor sorteado foi: {menor}')
"""

# Solução apresentada na aula

from random import randint

tupla = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f'Valores sorteados foram: {tupla}')
print(f'O maior valor sorteado foi {max(tupla)}')
print(f'O menor valor sorteado foi {min(tupla)}')
