# Variáveis de ambiente com Python
# Para variáveis de ambiente
# Windows PS: $env:VARIAVEL="VALOR" | dir env:
# Linux e Mac: export NOME_VARIAVEL="VALOR" | echo $VARIAVEL
# Para obter o valor das variáveis de ambiente
# os.getenv ou os.environ['VARIAVEL']
# Para configurar variáveis de ambiente
# os.environ['VARIAVEL'] = 'valor'
# Ou usando python-dotenv e o arquivo .env
# pip install python-dotenv
# from dotenv import load_dotenv
# load_dotenv()
# https://pypi.org/project/python-dotenv/
# OBS.: sempre lembre-se de criar um .env-example
#       nunca mande nenhum .env para os seus repositórios

# para criar uma variável temporaria no windows usa-se:
# $env:SENHA="MINHA SENHA"
# e depois 'dir env:' para olhar todas as suas variaveis locais

import os

#pegando a variavel do sistema operacional 
senha = os.getenv('SENHA')
print(senha)

# ---------------------------------------------------

from dotenv import load_dotenv #type: ignore

#caso exista um .env no programa ele vai carregar
load_dotenv()

#environ pega literalmente TUDO
# print(os.environ)

print(os.getenv('BD_PASSWORD'))





# ---------------------------------------------------

# python-dotenv é uma biblioteca Python que permite que você faça uso de arquivos de configuração para armazenar e acessar as suas variáveis de ambiente de forma mais fácil e segura em seus projetos.

# As variáveis de ambiente são valores que podem ser usados em seu código e que podem variar dependendo do ambiente em que o seu código está sendo executado (por exemplo, o ambiente de produção ou o ambiente de desenvolvimento).

# Para utilizar o python-dotenv, basta instalá-lo com o pip e, em seguida, adicionar um arquivo chamado .env na raiz do seu projeto.

#     # Ative seu ambiente virtual
#     pip install python-dotenv

# Esse arquivo deve conter as suas variáveis de ambiente e seguir o seguinte formato:

#     # .env
#     VARIAVEL_DE_AMBIENTE_1=valor
#     VARIAVEL_DE_AMBIENTE_2=valor
#     VARIAVEL_DE_AMBIENTE_3=valor

# Em seu código, você pode acessar essas variáveis usando o módulo os e a função os.getenv(), por exemplo:

#     import os
     
#     valor_da_variavel_1 = os.getenv("VARIAVEL_DE_AMBIENTE_1")

# O python-dotenv funciona lendo o arquivo .env e adicionando as variáveis de ambiente ao ambiente do sistema operacional, de forma que elas fiquem disponíveis para seu código usando a função os.getenv().

# Isso é útil, por exemplo, para não expor senhas ou outras informações 
# confidenciais em seu código ou em repositórios de código compartilhados, 
# pois o arquivo .env pode ser adicionado ao .gitignore para não ser incluído 
# nos commits. Crie um .env-example para exemplificar como usar o seu programa com valores fictícios.

# Além disso, o python-dotenv também permite que você use um arquivo 
# .env para armazenar valores de configuração específicos de cada ambiente, 
# o que pode ser útil quando você estiver trabalhando em um projeto com diferentes 
# ambientes de desenvolvimento, teste e produção.
# Doc: https://pypi.org/project/python-dotenv/