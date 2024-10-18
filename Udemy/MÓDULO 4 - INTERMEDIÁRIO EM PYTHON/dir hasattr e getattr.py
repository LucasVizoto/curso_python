# dir, hasattr e getattr
# esses metodos também podem ser usados no console do debugger
#
# dir mostra todas as coisas que podem ter no que foi passado
# has attr -> verifica se tem algum valor ali no parametro
#  get attr -> pega algum valor apontado
string = 'lucas'
metodo = 'lower'

if hasattr(string, metodo):
    print(f'Existe {metodo}')
    print(getattr(string, metodo)())
else:
    print(f'Não existe {metodo}')
