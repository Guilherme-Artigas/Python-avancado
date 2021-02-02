"""Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante a função input() do python, só
que fazendo a validação para aceitar somente um valor numérico. Ex: n = leiaInt('Digite um n')"""


def leiaInt(p1):
    ok = False
    valor = 0
    while True:
        n = str(input(p1))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO! Digite um número inteiro valido.\033[m')
        if ok:
            break
    return valor


# Programa Principal
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}.')
