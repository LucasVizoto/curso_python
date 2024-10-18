# Polimorfismo em Python Orientado a Objetos
# Polimorfismo é o princípio que permite que
# classes deridavas de uma mesma superclasse (classes que herdam)
# tenham métodos iguais (com mesma assinatura)
# mas comportamentos diferentes.
# Assinatura do método = Mesmo nome e quantidade de parametros (assinatura é tudo que tem no método)
# de parâmetros (retorno não faz parte da assinatura)
# Opinião + princípios que contam:
# Assinatura do método: nome, parâmetros e retorno iguais

# SO"L"ID - cada letra nesse SOLID representa um princípio

# Princípio da substituição de liskov
# Objetos de uma superclasse devem ser substituíveis
# por objetos de uma subclasse sem quebrar a aplicação.

#onde você usar uma super classe, qualquer subclasse dessa classe deve utilizar o método

#exemplo é o exerciocio de Mixin no log

# Sobrecarga de métodos (overload) 🐍 = ❌ (o python não suporta)
# Sobreposição de métodos (override) 🐍 = ✅

from abc import ABC, abstractmethod
class Notification(ABC):
    def __init__(self, msg) -> None:  #O init sempre retorna None,  a setinha indica quq deve retornar (pro python nn significa nada ksksk mas mostra pra quem é dev o que a função retorna) Type Anotations | Type Hintinng
        self.msg = msg

#o que é uma notificação? pode ser uma mensagem, pode ser uma multa, pode ser uma oferta
# percebe que isso é algo abstrato

#para saber se um programa é abstrato ou não se pegunte:
# FAZER O QUE? (CASO DO LOG(VOU LOGAR O QUE?), VOU MANDAR O QUE DE NOTIFICAÇÃO?)
    @abstractmethod
    def send_notification(self) -> bool: ... 

class EmailNotification(Notification):
    def send_notification(self) -> bool:
        print('Email: enviando', self.msg)
        return True
    
class WhatsappNotification(Notification):
    def send_notification(self, person = None)-> bool:
        if person:
            print(f'{person} enviou a mensagem: {self.msg}')
            return True
        

n = WhatsappNotification('testando notificação')
n.send_notification('Bia')

# OBSERVAÇÃO EXTREMAMENTE IMPORTANTE, os nomer da classe abstrata precisam ser o mesmo se não ele não irá instanciar

#apartir daqui de fato vira polimorfismo
def __notificar_exemple(notification: str) : #da mesma forma como a setinha não interfere, esses dois pontos servem apenas para definir o tipo que deve ser esse parâmetro
    #isso ajuda o vs code a passar os metodos de string pra cá e indica para outros dev o que a função deve retornar pra não quebrar o código
    notification


def notificar(notification: Notification) : #da mesma forma como a setinha não interfere, esses dois pontos servem apenas para definir o tipo que deve ser esse parâmetro
    #isso ajuda o vs code a passar os metodos de Notification pra cá e indica para outros dev o que a função deve retornar pra não quebrar o código
    notificacao_enviada = notification.send_notification()
#se vc passar o curso no método, vai ver que ele retorna um booleano (coisa que foi definida pela setinha)
    if notificacao_enviada:
        print ("Notificacao enviada")
    else:
        print ("ERRO AO ENVIAR NOTIFICAÇÃO")

email_notification = (EmailNotification('Love u'))
notificar(email_notification)

