def contador(i, f, p):
    """
    Função de contagem.
    :parameter i: Início da contagem
    :parameter f: Fim da contagem
    :parameter p: Passo da contagem
    :return: Sem Retorno
    """
    indice = i
    while indice <= f:
        print(f'{indice}', end='.. ')
        indice += p
    print('FIM!')


contador(1, 15, 1)
help(contador)


# Conceito de Parâmetro opcional
def somar(p1=0, p2=0, p3=0):
    """
    Faz a soma de três valores e mostra o resultado na tela.
    :param p1: Primeiro valor lido na chamada da função.
    :param p2: Segundo valor lido na chamada da função.
    :param p3: Terceiro valor lido na chamada da função.
    Todos os valores são opcionais, caso nao seja passado nenhuma valor para dentro dos parâmetros os valores padrões
    serão 0.
    Função criada por Guilherme Artigas, aluno do CursoemVideo.
    """
    soma = p1 + p2 + p3
    print(f'A soma vale {soma}')


somar(6, 7, 8)
somar(3, 8)
