
class Multiplicar:
    def __init__(self,func):
        self.func = func

    def __call__(self, *args,**kwds):
        print('INIT', args, kwds)
        return self.func(*args, **kwds)
@Multiplicar
def multiplicacao(x,y):
    return x*y

doisXdois = multiplicacao(8,5)
print(doisXdois) 