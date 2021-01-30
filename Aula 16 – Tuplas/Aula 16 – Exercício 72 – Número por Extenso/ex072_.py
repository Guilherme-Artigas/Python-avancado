""""
Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero a vinte.

Seu programa deverá ler um número pelo teclado entre (0 e 20) e mostra-lo por extenso.
"""
extenso = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Catorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

# Minha solução
"""
controle = True
n = 0
while controle == True:
    n = int(input('Digite um número entre [0 e 20]: '))
    if n < 0 or n > 20:
        print(f'Você digitou um valor invalido! {n}, por favor digite o valor indicado... ')
        controle = True
    else:
        for indice in range(len(extenso)):
            if n == indice:
                print(f'Você digitou o número {extenso[indice]}')
        controle = False
"""

# Solução mostrada na aula

while True:
    n = int(input('Digite um número entre 0 e 20: '))
    if 0 <= n <= 20:  # n >= 20 and n <= 20, eu escreveria dessa forma, porem, o python sugere outra.
        break
    print('Tente novamente. ', end='')
print(f'Você digitou o número {extenso[n]}')
