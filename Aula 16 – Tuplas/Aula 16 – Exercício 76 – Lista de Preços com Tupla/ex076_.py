""""
crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços. Na sequencia
No final, mostre uma listagem de preços organizando os dados em forma tabular.
Ex dado na Aula: listagem = ('Pão', 1, 'Leite', 3.50, 'Frango', 10.90)
"""

listagem = ('Placa mãe', 720, 'Processador', 995.70, 'Gabinete', 219, 'Fonte', 275, 'Memoria ram', 250, 'Placa de video', 1600, 'Armazenamento', 208)
print('*' * 40)
print(f'{"* LISTA DE PREÇOS *":^40}')
print('*' * 40)
for c in range(0, len(listagem), 2):
    print(f'{listagem[c]:.<28} ', end='')
    for c2 in range(c + 1, len(listagem)):
        print(f'R$ {listagem[c2]:.2f}')
        break
print('*' * 40)
