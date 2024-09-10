# Implementando o protocolo do Iterator em Python
# Essa é apenas uma aula para introduzir os protocolos de collections.abc no
# Python. Qualquer outro protocolo poderá ser implementando seguindo a mesma
# estrutura usada nessa aula.
# https://docs.python.org/3/library/collections.abc.html
from collections.abc import Sequence

class MyList(Sequence):

    def __init__(self):
        self._data = {}
        self._index = 0
        self._next_index = 0
        
    def append(self, *values):
        for value in values:
            self._data[self._index] = value
            self._index += 1

    def __len__(self)-> int:
        return self._index
    
    def __getitem__(self, index):
        # print('getitem', index)
        return self._data[index]

    def __setitem__(self, index, value):
        self._data[index] = value
    
    def __iter__(self):
        return self
    #a propria lista é um iterator dela

    def __next__(self):
        if self._next_index >= self._index:
            self._next_index = 0
    #como o index só vai aumentando este next é um tratamento de erro
    # para quando a soma passar do valor, ele der raise no erro e continuar o código
            raise StopIteration
        
        value = self._data[self._next_index]
        self._next_index += 1
        return value
    

    # realizando teste local
if __name__=='__main__':
    lista = MyList()
    lista.append('Lucas')
    lista.append(2)
    print (lista[0])
    print ('Tamanho:', len(lista))
    
    
    lista[0] = 'Beatriz'
    lista.append('Vizoto', 'Meleti')

    for item in lista:
        print('Iterando:', item)