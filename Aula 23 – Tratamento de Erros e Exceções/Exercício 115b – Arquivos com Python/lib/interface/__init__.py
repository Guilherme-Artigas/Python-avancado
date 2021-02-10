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


def linha(tam=22):
    return '+-' * tam

def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    indice = 1
    for item in lista:
        print(f'\033[33m{indice}\033[m - \033[34m{item}\033[m')
        indice += 1
    print(linha())
    opc = leiaInt('\033[32mSua Opção: \033[m')
    return opc
