n = 5


def teste():
    a = 2
    print(f'Dentro da função teste n vale {n}')
    print(f'Dentro da função, a  vale {a}')


print(f'Fora da função, n vale {n}')
teste()
print(f'Fora da função, a vale não existe :(')
