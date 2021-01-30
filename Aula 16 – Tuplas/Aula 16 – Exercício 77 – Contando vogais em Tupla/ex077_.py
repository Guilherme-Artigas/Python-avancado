""""
Crie um programa que tenha uma tupla com várias palavras (não usar acentos). depois disso, você deve mostrar
para cada palavra, quais são as suas vogais.
"""
tupla = ('Programador', 'Atacante', 'Rafaela', 'Python', 'Maria julia', 'Monte Horebe')
for palavra in tupla:
    print(f'\nNa palavra {palavra.upper()} temos: ', end='')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
