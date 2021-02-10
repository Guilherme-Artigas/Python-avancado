"""Reescreva a função leiaInt() que fizemos no desafio 104, inlcuindo agora a possibilidade da digitação de um número
de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade."""


def leiaInt(p1):
    while True:
        try:
            n = int(input(p1))
        except (ValueError, TypeError):
            print(f'\033[0;31mERRO: por favor, digite um número inteiro valido.\033[m')
            continue
        except (KeyboardInterrupt):
            print(f'Entrada de dados interrompida pelo usuario.')
            return 0
        else:
            return n


def leiaFloat(p1):
    while True:
        try:
            f = float(input(p1))
        except (ValueError, TypeError):
            print(f'\033[0;34mERRO: por favor, digite um número flutuante valido.\033[m')
            continue
        else:
            return f


# Programa Principal
n = leiaInt('Digite um número inteiro: ')
print(f'O valor digitado foi {n}')
f = leiaFloat('Digite um número flutuante: ')
print(f'O valor digitado foi {f}')
