''' 
 Ambientes virtuais em Python (venv)
 Um ambiente virtual carrega toda a sua instalação
 do Python para uma pasta no caminho escolhido.
 Ao ativar um ambiente virtual, a instalação do
 ambiente virtual será usada.
 venv é o módulo que vamos usar para
 criar ambientes virtuais.
 Você pode dar o nome que preferir para um
 ambiente virtual, mas os mais comuns são:
 venv env .venv .env
 É basicamente uma pasta

 **** python -m venv (nome do ambiente virtual, recomendo por venv tbm)

 na pasta lib fica tudo o que você instalar de terceiros

 scripts são todos os executaveis que você pose fazer no seu ambiente virtuaal
    - activate para ativar
    - deactivate é para literalmente desativar o ambiente
    - pip - intalador de pacotes 
 pip intala do Python package index

 ****gcm python -Syntax (mostra o path do python)
 usar isso para ver qual python seu programa está usando
  - no terminal de python serve para chamer um comando

 quando você usa o ambiente virtual ele muda o Python que vai ser 
 utilizado, por isso é importante verificar


 para ativar o ambiente você precisa chamar no terminal o 
**** arquivo do activate
****  .\venv\Scripts\activate
****  pip --version (versão do pip)
**** para desativar o ambiente virtual, basta digitar: deactivate 
     no terminal e ele irá parar


 quando ativar o venv , lembrar de mudar o interpretador para o 
 "versão_mais_atual_Python" 'venv' venv
 para evitar de instalar no Python global

**** pip install pymysql
**** python -m pip install pymysql
            isso é para instalar coisas no ambiente virtual
            para desinstalar, basta trocar o install para unistall


**** pip freeze - mostra os pacotes intalados e suas versões

com o pip freeze a gente consegue montar um arquivo que chama requirements.txt (re gerar nosso venv)

não se manda a pasta quando vai exportar para o GitHub
cria-se um requirement.txt para dizer os documentos requeridos para rodar seu programa


****  pip freeze > requirements.txt
gera o requirement, guardando o noome e versão de cada coisa instalada
no seu ambiente



**** pip install -r requirements.txt
intala cada item e versão do requirement colocado como "parâmetro"

se você instalar mais itens no seu ambiente LEMBRE-SE de atualizar o requirement
para atualizar, basta colocar o mesmo código utilizado para criar


'''