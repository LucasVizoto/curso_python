# Positional-Only Parameters (/) e Keyword-Only Arguments (*)
# *args (ilimitado de argumentos posicionais)
# **kwargs (ilimitado de argumentos nomeados)
# 🟢 Positional-only Parameters (/) - Tudo antes da barra deve
# ser ❗️APENAS❗️ posicional.
# PEP 570 – Python Positional-Only Parameters
# https://peps.python.org/pep-0570/
# 🟢 Keyword-Only Arguments (*) - * sozinho ❗️NÃO SUGA❗️ valores.
# PEP 3102 – Keyword-Only Arguments
# https://peps.python.org/pep-3102/
def soma(a, b, /  ):
    print(a+b)
soma(1,2)    
# a barra faz com que ele aceite apenas posicionais, sendo assim, quando uma pessoa 
# passar algum argumento nomeado na chamada da função, ele irá dar raise num erro 

def soma_diferente( a, b, *, c):
    print(a+b+c)
soma(1,2, c=3)
# até o * são argumentos posicionais, mas depois dele você PRECISA nomear
# os argumentos