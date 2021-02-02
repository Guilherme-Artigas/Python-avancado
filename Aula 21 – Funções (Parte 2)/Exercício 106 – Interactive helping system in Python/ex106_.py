"""Faça um mini sistema que ultilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai
aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará. Importante: use cores."""
c = ('\033[m',      # 0 - Cor Padrão
     '\033[0;34m',  # 1 - Azul
     '\033[0;31m')  # 2 - Vermelho )


def ajuda(p1):
    iniciofim(f'Acessando o manual do comando \'{p1}\'', 2)
    help(p1)


def iniciofim(p1, p2=0):
    tamanho = len(p1) + 4
    print(c[p2], end='')
    print('~' * tamanho)
    print(f'  {p1}')
    print('~' * tamanho)
    print(c[0], end='')


# Programa Principal
while True:
    iniciofim('SISTEMA AJUDA PyHelp', 1)
    comando = str(input('Função ou biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
iniciofim('ATÉ LOGO', 1)
