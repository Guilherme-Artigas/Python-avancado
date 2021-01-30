pessoas = {'nome': 'Guilherme', 'sexo': 'M', 'idade': 28}
# print(f'{pessoas["nome"]}')  # Importante uso de aspas duplas para não dar erro.
# print(pessoas.keys())
# print(pessoas.values())
# print(pessoas.items())

# Pegando o valor dentro do dicionário por chave.
"""for chave in pessoas.keys():
    print(chave)"""

# Pegando o valor dentro do dicionário por valor.
"""for valor in pessoas.values():
    print(valor)"""

# Pegando a chave e valor de forma simultanea no mesmo laço.
"""for chave, valor in pessoas.items():
    print(f'{chave:6}: {valor}')"""

# Apagando valores do dicionário
"""del pessoas['sexo']
print(pessoas)"""

# Atribuição de valores não é feita com .append()! e sim dessa forma...
"""pessoas['nome'] = 'João'
print(pessoas)"""

# Adicionando elementos...
"""pessoas['peso'] = 96.4
print(pessoas)"""
