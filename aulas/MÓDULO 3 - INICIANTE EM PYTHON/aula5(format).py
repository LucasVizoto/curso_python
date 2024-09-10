a= 'A'
b = 'B'
c = 1.1
formato = 'a={}'.format(a,b,c)
print(formato) #Parâmetros no format

# As chaves são usadas pra indicar o lugar que vai o parâmetro
formato1 = 'a={1}'.format(a,b,c)    # 0 1 2
print(formato1) #Parâmetros usando a posição comom chamada

# outra forma bem interessante de se fazer é nomeando os parâmetros
formato2 = 'a={nome1}, b={nome2}, c={nome3} '.format(nome1=a,nome2=b,nome3=c)
#TUDO QUE VIER DEPOIS DE UM PARAÂMETRO NOMEADO DEVE SER NOMEADO TAMBÉM