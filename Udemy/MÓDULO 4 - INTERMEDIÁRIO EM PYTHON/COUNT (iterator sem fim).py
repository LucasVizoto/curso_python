#count é um iteratod sem fim (itertools)
from itertools import count
c2 = count(8, step=4) #Pode-se escrever também com o step escrito
c1 = count(8, 8) #apenas inicio e step 
r1 = range(10, 100, 8) #inicio fim e step
# todos os dois vão de 8 em 8
print('c1', hasattr(c1, '__iter__')) # iterável?
print('c1', hasattr(c1, '__next__')) # iterator?

for i in c1:
    if i>=100:
        break
    print(i)
for i in r1:
    if i>=100:
        break
    print(i)
