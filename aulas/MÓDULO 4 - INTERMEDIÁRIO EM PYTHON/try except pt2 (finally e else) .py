# https://docs.python.org/pt-br/3/library/exceptions.html
# biblioteca do Python com muito mais coisas sobre o assunto


# try except, else e finally
# tome cuidado com o ato de "Silenciar" erros

try: 
    a = 18
    b = 0
    c = a/b
    print(c)
    print(d)
    print(' dfjasfsio' [2000])
except ZeroDivisionError:
    print('Não é possível dividir por zero')
except NameError:
    print('A variável não existe')    
# except Exception:
#     print('Algum erro ocorreu')
#     #Exception cai aqui quando aconterce qualquer erro não tratado   
except (TypeError, ValueError, IndexError) as error:   #as captura o erro
    print('TypeError + IndexError + ValueError')
    print(f'MSG: {error}') # Mensagem do erro
    print(f'Nome_Classe: ', error.__class__.__name__) #Pega o Nome do Erro indo na classe de error
# NÃO É NADA RECOMENDADO FAZER ISSO, mas dá    

#------------------------------------------------------------------------------------------------------

# try except, else finally

try: 
    ...
finally: # um bloco que SEMPRE será executado no Try Except, mesmo com o erro
    ...

try: 
    print('ABRIR ARQUIVO')
    8/0
finally:
    print('FECHAR ARQUIVO')    

# else vem depois do except, não é muito útil, mas tem ksks

