def fatorial(p1):
    f = 1
    indice = p1
    while indice >= 1:
        f *= indice
        indice -= 1
    return f


# Programa Principal
num = int(input('Digite um valor: '))
fat = fatorial(num)
print(f'O fatorial de {num} é {fat}')
