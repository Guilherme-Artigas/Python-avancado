"""Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um arquivo de texto
simples. O sistema só vai ter duas opções: cadastrar uma nova pessoa e listar todas as pessoas cadastradas."""
from lib.interface import *
from lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arqExiste(arq):
    criararquivo(arq)

while True:
    res = menu(['Ver Pessoas Cadastradas', 'Cadastrar Nova Pessoa', 'Sair do Sistema'])
    if res == 1:
        # Opção de listar o conteúdo de um arquivo!
        lerArquivo(arq)
    elif res == 2:
        cabecalho('Opção 2')
    elif res == 3:
        cabecalho('Saindo do sistema... Até logo!')
        sleep(2)
        break
    else:
        print('\033[31mERRO! Digite um opção valida.\033[m')
        sleep(2)
