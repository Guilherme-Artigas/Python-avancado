try:
    n1 = int(input('Numerador: '))
    n2 = int(input('Denominador: '))
    res = n1 / n2
except (ValueError, TypeError):
    print(f'Tivemos um problema com os tipos de dados que você digitou.')
except ZeroDivisionError:
    print(f'Não é possivel dividir um número por zero!')
except KeyboardInterrupt:
    print(f'O usúario preferiu não informar os dados!')
except Exception as erro:
    print(f'O erro encontrado foi {erro.__cause__}')
else:  # Clausula else, finaly são opcionais.
    print(res)
finally:
    print('Volte sempre muito obrigado!')
