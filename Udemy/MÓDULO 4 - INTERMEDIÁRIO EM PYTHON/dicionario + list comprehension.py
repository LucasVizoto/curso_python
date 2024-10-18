produto = {
    'nome': 'Martelo',
    'preco'  : 2.5,
    'categoria' : 'Escritório'
}

for chave, valor in produto.items():
    print(chave, valor)


dicionario = {chave:valor.upper() if isinstance(valor, str) else valor for chave, valor in produto.items()}    
# isinstance -> Verificar se o primeiro parametro é do tipo do segundo retornando True ou False
#valor vai ficar maiúsculo se valor for uma string, senão recebe apenas valor , para cada chave em item nos items do dicionário produto 
print(dicionario)
