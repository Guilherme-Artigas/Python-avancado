"""Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma
pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições."""


# Minha Solução
"""def voto(p1):
    data_atual = date.today()
    idade = data_atual.year - p1
    if idade < 16:
        print(f'Idade: {idade} anos, VOTO Negado!')
    elif 16 <= idade < 18:
        print(f'Idade: {idade} anos, VOTO Opcional!')
    else:
        print(f'Idade: {idade} anos, VOTO Obrigatório!')"""


# Programa Principal
"""print('+-' * 20)
ano = int(input('Ano de nascimento: '))
voto(ano)"""

# Solução apresentada na aula


def voto(p1):
    from datetime import date
    ano_atual = date.today().year
    idade = ano_atual - p1
    if idade < 16:
        return f'Idade: {idade} anos, NÃO VOTA!'
    elif 16 <= idade < 18 or idade > 65:
        return f'Idade: {idade} anos, VOTO OPCIONAL!'
    else:
        return f'Idade: {idade} anos, VOTO OBRIGATÓRIO!'


# Programa Principal
nasc = int(input('Em que ano você nasceu: '))
print(voto(nasc))
