""""
Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
Caso o número já exista lá dentro, ele não sera adicionado. No final, serão exibidos todos os valores únicos digitados,
em ordem crescente.
"""
# Minha Solução
from time import sleep
lista = list()  # lista = [] 2º opção para atribuir
controle = controle2 = True
laco = valor = 0
while controle == True:
    laco += 1
    valor = int(input(f'Digite o {laco}º valor: '))
    if valor in lista:
        print('Valor duplicado! Não vou adicionar.')
    else:
        print('Valor adicionado com sucesso.')
        lista.append(valor)
    controle2 = True
    while controle2 == True:
        resposta = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
        if resposta == 'S':
            controle = True
            controle2 = False
        elif resposta == 'N':
            print('=-' * 30)
            lista.sort()
            print(f'Você digitou os valores: {lista}')
            print('Obrigado... programa sendo encerrado!')
            sleep(3)
            print('... AGUARDE!')
            sleep(1)
            print('Encerrado!')
            controle = False
            controle2 = False
        else:
            print(f'Você digitou uma opção invalida! Por favor digite [S/N] ... ')
            controle2 = True
