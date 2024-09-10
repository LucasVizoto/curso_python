def adiciona_clientes(nome, lista=[]):
    lista.append(nome)
    return lista
    
cliente1 = adiciona_clientes('Lucas')
adiciona_clientes('Beatriz', cliente1)
print(cliente1)
#forma "errada" de se fazer. pois nesse caso, há uma criação de um valor mutável nos parametros da funcao e certos casos podem gerar um conflito


def adiciona_clientes_certo(nome, lista=None):
    if lista is None:
        lista=[]
    lista.append(nome)
    return lista
    
cliente2 = adiciona_clientes_certo('Lucas')
adiciona_clientes('Beatriz', cliente2)
cliente2.append('Jude')
cliente2.append('Cardan')
print(cliente2)