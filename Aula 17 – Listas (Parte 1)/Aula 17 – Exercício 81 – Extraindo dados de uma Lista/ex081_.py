""""
Crie um programa que vai ter vários números e colocar em uma lista. Depois disso mostre:

A) Quantos números foram digitados.
B) A lista de valores ordenada de forma decrescente.
C) Se o valor 5 foi digitado e esta ou não na lista.
"""
# Minha solução
"""lista = []
controle = True
laco = 0
while controle == True:
    valor = int(input('Digite um valor: '))
    lista.append(valor)
    laco += 1
    resposta = True
    while resposta == True:
        resposta = str(input('Quer continuar: [S/N]: ')).strip().lower()[0]
        if resposta == 's':
            controle = True
            resposta = False
        elif resposta == 'n':
            controle = False
            resposta = False
        else:
            print('Valor de resposta invalido... Tente de novo!')
            resposta = True
print('=-' * 30)
print(f'A - Foram digitados {laco} valores.')
lista.sort(reverse=True)
print(f'B - Lista ordenada de forma decrescente: {lista}')
if 5 in lista:
print('C - Valor 5 foi digitado e esta na lista!')
else:
print('C - Valor 5 não foi digitado.')"""
# Solução apresentada na aula
lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    resposta = str(input('Quer continuar? [S/N]: '))
    if resposta in 'Nn':
        break
print('*-' * 30)
print(f'Você digitou {len(lista)} elementos.')
lista.sort(reverse=True)
print(f'Lista ordenada de forma decrescente é: {lista}')
if 5 in lista:
    print('O valor foi esta dentro da lista.')
else:
    print('O valor 5 não foi encontrado dentro da lista.')
