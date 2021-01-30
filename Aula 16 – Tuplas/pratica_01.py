lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata frita')

# Leitura dos elementos da tupla, sem mostrar a posição
"""for comida in lanche:
    print(comida)"""

# Leitura dos elementos usando o FOR, possibilitando mostrar a posição dos elementos dentro da tupla
"""for c in range(0, len(lanche)):
    print(lanche[c])"""

# Outra forma da leitura da tupla, usando 2 variaveis para estrutura for
for pos, comida in enumerate(lanche):
    print(f'{lanche[pos]} - lanche {pos}')

print(sorted(lanche))  # Colocando a tupla em ordem.
