"""Crie um programa que tenha um função fatorial() que receba dois parâmetros: o primeiro que indique o número a
calcular e o outro chamado show, que sera um valor lógico (opcional) indicando se sera mostrado ou não na tela o
processo de calculo do fatorial."""


def f_fatorial(p1, p2=bool):
    """
    -> Calculo de fatorial de um valor.
    :param p1: Valor escolhido pelo usuário para ser calculado o fatorial.
    :param p2: Usuário responde a pergunta, caso resposta positiva é mostrado o calculo na tela.
    :return: Retorna o valor do fatorial escolhido pelo usuário.
    """
    from time import sleep
    indice = p1
    fatorial = 1
    print('+-' * 15)
    while indice >= 1:
        fatorial *= indice
        if p2:  # if p2 == True
            print(f'{indice}', end='')
            if indice > 1:
                print(' x ', end='')
            else:
                print(f'{" ="} {fatorial}')
            sleep(0.5)
        indice -= 1
    if not p2:  # if p2 == False
        print(fatorial)


# Programa principal
valor = int(input('Digite um valor para calcular o fatorial: '))
while True:
    show = str(input('Deseja mostrar o calculo na tela? [S/N]: ')).strip().upper()[0]
    if show == 'S':
        mostrar = True
        break
    elif show == 'N':
        mostrar = False
        break
    else:
        print('Resposta invalida! digite S ou N.')


f_fatorial(valor, mostrar)
