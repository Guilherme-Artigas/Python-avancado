"""def fatorial(p1=1):
    f = 1
    for indice in range(p1, 0, -1):
        f *= indice
    return f


f1 = fatorial(6)
f2 = fatorial(8)
f3 = fatorial()
print(f'Os resultados são {f1}, {f2}, {f3}')"""


def parouimpar(p1=0):
    if p1 % 2 == 0:
        return True
    else:
        return False


v = int(input('Digite um valor: '))
if parouimpar(v):
    print('É Par!')
else:
    print('Não é Par!')
