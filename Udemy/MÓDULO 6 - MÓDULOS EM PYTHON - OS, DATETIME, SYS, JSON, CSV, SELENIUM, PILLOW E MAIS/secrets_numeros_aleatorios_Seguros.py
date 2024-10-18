# secrets gera numeros aleatórios seguros
# a partir do Python 3.6


import secrets
import string as s
from secrets import SystemRandom as Sr

#forma correta de gerear uma senha de forma aleatória
print(s.ascii_letters + s.digits + s.punctuation)
# a biblioteca string retornou todos os caracteres 
#(letras maiúsculas, minúsculas, numeros e caracteres especiais)

print(Sr().choices(s.ascii_letters + s.digits + s.punctuation), k=12)
#retona uma lista de 12 caracteres onde todos são aleatórios

print(''.join(Sr().choices(s.ascii_letters + s.digits + s.punctuation), k=12))
# Com esse join, unimos toda a lista em uma string(senha) de 12 caracteres










print(secrets.randbelow(100)) # abaixo do valor passado 
print(secrets.choice([10,11,12,18,5]))

random = secrets.SystemRandom()
# está usando a aleatoriedade do seu sistema operacional
# neste caso substitui o import random pela variavel random com o 
# secrets.SystemRandom()

#--------------------------------------------------------

# copiando da aula anterior para mostrar como de fato fica mais randomizado

random.seed(10)
#agora não funciona pois não utilizamos mais o time.time()

# random.randrange(início, fim, passo)
#   -> Gera um número inteiro aleatório dentro de um intervalo específico
r_range = random.randrange(10, 20, 2)
# print(r_range)

# random.randint(início, fim)
#   -> Gera um número inteiro aleatório dentro de um intervalo "sem passo"
r_int = random.randint(10, 20)
# print(r_int)

# random.uniform(início, fim)
#   -> Gera um número flutuante aleatório dentro de um intervalo "sem passo"
r_uniform = random.uniform(10, 20)
# print(r_uniform)

# random.shuffle(SequenciaMutável) -> Embaralha a lista original
nomes = ['Luiz', 'Maria', 'Helena', 'Joana']
# random.shuffle(nomes)
# ELE MUDA A LISTA ORIGINAL, LOGO, TOME CUIDADO
# print(nomes)

# random.sample(Iterável, k=N) K É O TAMANHO DO SAMPLE
#   -> Escolhe elementos do iterável e retorna outro iterável (não repete)
novos_nomes = random.sample(nomes, k=3)
# print(nomes)
# print(novos_nomes)

# random.choices(Iterável, k=N)
#   -> Escolhe elementos do iterável e retorna outro iterável (repete valores)
# PODE ACABAR REPETINDO OS VALORES DA LISTA DURANTE O SAMPLE
novos_nomes = random.choices(nomes, k=3)
print(nomes)
print(novos_nomes)

# random.choice(Iterável) -> Escolhe um elemento do iterável
print(random.choice(nomes))