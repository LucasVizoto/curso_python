# raise - lançando exceções (erros)

# print(123)
# raise ValueError('DEU ERRO!')
# print(123)
# Você força o programa a dar esse erro, raise é usado para tratar erros

def nao_aceita_zero(d):
    if d == 0:
        raise ZeroDivisionError('Não existe divisão por zero')

def deve_ser_int_ou_float(n):
    tipo_n = type(n)
    if not isinstance(n, (float, int)):
        raise TypeError(
            f'"{n}" deve ser int ou float. '
            f'"{tipo_n.__name__}" enviado.'
        )
    return True


def divide(n, d):
    deve_ser_int_ou_float(n)
    deve_ser_int_ou_float(d)
    nao_aceita_zero(d)
    return n / d

print(divide(8,0))
# a,b = map(int,input('valores ').split())
