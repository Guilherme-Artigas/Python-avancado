"""
Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um
boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
"""
nome = []
notas = []
medias = []
boletim = []
while True:
    nome.append(str(input('Nome: ')))
    notas.append(float(input('Nota 1: ')))
    notas.append(float(input('Nota 2: ')))
    r = str(input('Quer continuar? [S/N]: ')).strip().lower()[0]
    if r in 'Nn':
        boletim.append(nome[:])
        boletim.append(notas[:])
        for indice in range(0, len(boletim[1]), 2):
            medias.append((boletim[1][indice] + boletim[1][indice + 1]) / 2)
        boletim.append(medias[:])
        nome.clear()
        notas.clear()
        medias.clear()
        break
print('+-' * 30)
print()
print('No.  Nome                      Média')
print('-' * 40)
for indice, valor in enumerate(boletim[0]):
    print(f'{indice}    {boletim[0][indice]:25}  {boletim[2][indice]:.2f}')
print('-' * 40)
controle = True
while controle:
    resposta = str(input('Quer ler as notas bimestrais de algum aluno? [S/N]: ')).strip().upper()[0]
    if resposta == 'S':
        quantidade_aluno = len(boletim[0])
        aluno = int(input(f'Digite o código do aluno entre [{0, quantidade_aluno - 1}]: '))
        print(f'Notas de {boletim[0][aluno]}: ', end='')
        c = 0
        for indice in range(0, len(boletim[1]), 2):
            if aluno == c:
                print(f'[{boletim[1][indice], boletim[1][indice + 1]}]')
            c += 1
        controle = True
    elif resposta == 'N':
        controle = False
    else:
        print('Resposta invalida!')
        controle = True
