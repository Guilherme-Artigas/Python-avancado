def aumentar(p1=0, p2=0, p3=False):
    """
    -> Calcula o aumento de um determinado preço, retornando o resultado com ou sem formatação.
    :param p1: Preço a ser reajustado.
    :param p2: Qual é a porcentagem do aumento.
    :param p3: Quer a saída formatada ou não.
    :return: O valor reajustado, com ou sem formato.
    """
    res = p1 + (p1 * p2 / 100)
    return res if p3 is False else moeda(res)


def diminuir(p1=0, p2=0, p3=False):
    res = p1 - (p1 * p2 / 100)
    return res if p3 is False else moeda(res)


def dobro(p1=0, p2=False):
    res = p1 * 2
    return res if p2 is False else moeda(res)


def metade(p1=0, p2=False):
    res = p1 / 2
    return res if p2 is False else moeda(res)


def moeda(p1, m='R$'):
    return f'{m}{p1:>.2f}'.replace('.', ',')


def resumo(p1=0, p2=10, p3=5):
    print('+-' * 15)
    print('RESUMO DO VALOR'.center(30))
    print('+-' * 15)
    print(f'Preço analisado: \t{moeda(p1)}')
    print(f'Dobro do preço: \t{dobro(p1, True)}')
    print(f'Metade do preço: \t{metade(p1, True)}')
    print(f'{p2}% de aumento: \t{aumentar(p1, p2, True)}')
    print(f'{p3}% de redução: \t{diminuir(p1, p3, True)}')
    print('+-' * 15)


def leiadinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada.strip() == '':
            print(f'\033[0;31mERRO: \"{entrada}\" é um preço inválido!\033[m')
        else:
            valido = True
            return float(entrada)
