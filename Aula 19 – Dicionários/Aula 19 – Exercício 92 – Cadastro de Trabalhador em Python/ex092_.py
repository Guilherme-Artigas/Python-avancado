"""Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário
se por a caso a CTPS for diferente de zero, o dicionário receberá também o ano de contratação e o salário. Calcule e
acrescente, alem da idade, com quantos anos a pessoa vai se aposentar. Considerando 35 anos de contribuição para a
aposentadoria."""
from datetime import date
cadastro = dict()
cadastro['nome'] = str(input('Nome: '))
ano_nascimento = int(input('Ano de nascimento: '))
ano_atual = date.today()
cadastro['idade'] = ano_atual.year - ano_nascimento
cadastro['ctps'] = int(input('Carteira de trabalho (0 não tem): '))
if cadastro['ctps'] != 0:
    cadastro['contratação'] = int(input('Ano de contratação: '))
    cadastro['salario'] = float(input('Salário: R$ '))
    cadastro['aposentadoria'] = (cadastro['contratação'] + 35) - ano_nascimento
print()
print('+-' * 40)
print('DADOS DO CIDADÃO: ')
print()
for chave, valor in cadastro.items():
    print(f'{chave:15}: {valor}')
