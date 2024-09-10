def soma (x:float, y:float)->float:
    return x+y

print(__name__)
#quando eu executar esse dunder method, ele irá indicar que esse cara é o main
# MAS se eu pegar e executar o app ele vai mostar o nome do arquivo
# pois ele está apenas importando daqui  

if __name__ == "__main__":
    print(soma(2, 3))
    print(soma(4.5, 6.7))

# por costume de outras linguagens, tem pessoas que também fazem assim:

def main():
    print(soma(2, 3))
    print(soma(4.5, 6.7))

if __name__ == "__main__":
    main()
# coloca-se tudo na main e depois apenas executa a função