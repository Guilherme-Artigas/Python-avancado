"""Crie um programa que leia nome, sexo, e idade de varias pessoas, guardando os dados de cada pessoa em um dicionário
e todos os dicionários em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) A média de idade do grupo.
C) Uma lista com todas as mulheres.
D) Uma lista com todas as pessoas com idade acima da média."""
cadastro = {}
lista = []
listaM = []
soma = media = totalP = 0
while True:
    cadastro['nome'] = str(input('Nome: '))
    while True:
        cadastro['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
        if cadastro['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    cadastro['idade'] = int(input('Idade: '))
    soma += cadastro['idade']
    if cadastro['sexo'] == 'F':
        listaM.append(cadastro['nome'])
    lista.append(cadastro.copy())
    resposta = str(input('Quer continuar? [S/N]: '))
    if resposta in 'Nn':
        break
print('+-' * 30)
totalP = len(lista)
media = soma / totalP
print(f' - O grupo tem {totalP} pessoas.')
print(f' - A média de idade é de {media:.1f} anos.')
print(f' - As mulheres cadastradas foram: {listaM}')
print(f' - Lista de pessoas que estão com idade acima da média: ')
for pessoa in lista:
    for chave, valor in pessoa.items():
        if pessoa['idade'] > media:
            print(f'  {chave}: {valor}', end=';   ')
    print()
