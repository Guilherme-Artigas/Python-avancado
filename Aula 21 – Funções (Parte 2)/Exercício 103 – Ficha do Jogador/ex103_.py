"""Faca um programa que tenha um função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e
quantos gols ele marcou. O programa devera ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido
informado corretamente."""


def ficha(p1, p2=0):
    """
    -> Função para cadastro de jogador.
    :param p1: Recebe o nome. Caso não informado o valor exibido sera <desconhecido>.
    :param p2: Recebe a quantidade de gols. Caso não informado o valor exibido é 0.
    :return: Retorna uma frase com nome e quantidade de gols.
    """
    if p1 == '':
        p1 = '<desconhecido>'
    if p2 == '':
        p2 = 0
    print(f'O jogador {p1} fez {p2} gol(s) no campeonato.')


# Programa principal
nome = str(input('Nome do Jogador: '))
gols = input('Número de gols: ')
ficha(nome, gols)
