# Funções recursivas e recursividade
# uma coisa que chama ela de volta
# - funções que podem se chamar de volta
# - úteis p/ dividir problemas grandes em partes menores
# Toda função recursiva deve ter:

# - Um problema que possa ser dividido em partes menores
# - Um caso recursivo que resolve o pequeno problema
# - Um caso base que para a recursão (return do valor)

# - fatorial - n! = 5! = 5 * 4 * 3 * 2 * 1 = 120
# https://brasilescola.uol.com.br/matematica/fatorial.htm
# quanto mais uniforme, mais fácil de fazer função recursiva
#stackOverfloe, cloca muitas coisas na callstack e para pra nn fritar teu pc

def recursiva(inicio=0, fim=10):
    print(inicio, fim)
    #caso de segurança para nn estourar o bagulho (Caso base)
    if inicio >= fim:
        return
    
    #problema maior - preciso contar de um número até outro (de um inicio até um final)
    inicio+=1 
    return recursiva(inicio, fim)

# meio inútil? SIM
# mas é importante saber disso, pois existem linguagens funcionais que trabalham 
# com a call de funções e não possuem os loops While, For e DoWhile (que são mais práticos no Python)

def fatorial (n):
    if n <= 1:
        return 1
    return n * fatorial(n-1)