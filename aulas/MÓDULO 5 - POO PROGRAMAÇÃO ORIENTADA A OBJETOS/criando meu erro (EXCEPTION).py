# Criando Exceptions em Python Orientado a Objetos
# Para criar uma exception em Python , você só precisa herdar de alguma
# exceção da linguagem. A recomendação da doc é herdar de Exception.

# criando exceções(comum colocar Error ao final)
# Levantando(raise) / lançando(trow) exceções
# https://docs.python.org/3/library/exceptions.html
# relançando exceções
# Adicionando notas em exceções (3.11.0)
#criando meu próprio erro

class MyError(Exception): ...
class AnotherError(Exception): ...
#sem meme KSKSKKSKSKS É SÓ ISSO
def levantar():
    exception_ = MyError('MENSAGEM DO MEU ERRO')
    raise exception_

try:    
    # 1/0 
    levantar()

except (MyError, ZeroDivisionError) as error: #as coisas chegarão em error como args
    print(error.__class__.__name__)
    print(error.args)
    print()
    exception_outro_error = AnotherError('Vou relançar uma exceção') #o rolê disso é que você relança uma exceção que alguém irá tratar em outra parte da sua equipe
    exception_outro_error.add_note('Anotação para comunicar o que está acontecendo')
    exception_outro_error.add_note('Você errou isso')
    exception_outro_error.__notes__ += error.__notes__.copy() # concatenando notas de erro
    raise exception_outro_error from error # dentro de uma exceção você lança uma outra exceção
