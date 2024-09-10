# Método especial __call__
# callable é algo que pode ser executado com parênteses
# Em classes normais, __call__ faz a instancia de uma classe 'callable'

class CallMe:
    def __init__(self,phone):
        self.phone = phone

    def __call__(self, *args, **kwargs):
        print("Calling", self.phone)

call1 = CallMe('16991926379')
# call1() dá erro pq por enquanto o objeto não é callablle (antes de definir o método call)
call1() #(depois que definido o méto call é possível chamá-lo, e assim que chamado, ele executa o que está nesse método)