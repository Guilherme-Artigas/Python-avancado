""""
Desenvolva um programa que leia 4 valores pelo teclado e guarde-os em uma tupla. no final mostre:

A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.
"""

# Minha solução
"""
n1 = int(input('Digite o 1º valor: '))
n2 = int(input('Digite o 2º valor: '))
n3 = int(input('Digite o 3º valor: '))
n4 = int(input('Digite o 4º valor: '))

tupla = (n1, n2, n3, n4)

controle = True
while controle == True:
    print('#' * 20)
    print(' - MENU DE OPÇÕES - ')
    print('#' * 20)
    print()
    print('A) Quantas vezes apareceu o valor 9.')
    print('B) Em que posição foi digitado o primeiro valor 3.')
    print('C) Quais foram os números pares.')
    opcao = str(input('Digite uma opção: ')).strip().upper()[0]
    print()

    if opcao == 'A' or opcao == 'a':
        print(' -- RESULTADO -- ')
        quantas = 0
        for c in range(0, len(tupla)):
            if tupla[c] == 9:
                quantas += 1
        print(f'Valor 9 apareceu {quantas} vez(es).')
        controle = False
    elif opcao == 'B':
        pos3 = 0
        print(' -- RESULTADO -- ')
        for c in range(0, len(tupla)):
            if tupla[c] == 3:
                pos3 = c + 1
        if pos3 > 0:
            print(f'O primeiro valor 3 foi digitado na posição {pos3}. ')
        else:
            print('O valor 3 não foi digitado nenhuma vez.')
        controle = False
    elif opcao == 'C':
        print(' -- RESULTADO -- ')
        print('Numeros pares digitados: ', end='')
        for c in range(0, len(tupla)):
            if tupla[c] % 2 == 0:
                print(tupla[c], ', ', end='')
        controle = False
    else:
        print('Você digitou uma opção invalida, por favor tente de novo...')
        print()
        controle = True
"""

# Solução apresentada na aula

tupla = (int(input('Digite o 1º valor: ')),
         int(input('Digite o 2º valor: ')),
         int(input('Digite o 3º valor: ')),
         int(input('Digite o 4º valor: ')))
print(f'Você digitou os valores: {tupla}')
print(f'O valor 9 apareceu {tupla.count(9)} vezes.')
if 3 in tupla:
    print(f'O valor 3 apareceu na {tupla.index(3) + 1}º posição')
else:
    print('O valor 3 não foi digitado!')
print('Os valores pares digitados foram ', end='')
for c in tupla:
    if c % 2 == 0:
        print(c, end=', ')
