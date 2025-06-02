# raise - lançando exceções

# print(123)
# raise ValueError ('Deu erro')
# print(456)

def nao_aceito_erro(d):
    if d == 0:
        raise ZeroDivisionError('Voce esta tentando dividir por 0')
    return True

def deve_ser_int_ou_float(n):
    tipo_n = type (n)
    if not isinstance(n, (float, int)):
        raise TypeError(
            f'"{n}" dever ser int ou float. '
            f'"{tipo_n.__name__}" enviado'
        )
    return True

def divide (n, d):
    deve_ser_int_ou_float(n)
    deve_ser_int_ou_float(d)
    nao_aceito_erro (d)
    return n / d

print(divide(8,'0'))