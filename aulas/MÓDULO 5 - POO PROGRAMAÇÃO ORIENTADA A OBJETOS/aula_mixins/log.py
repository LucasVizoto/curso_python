#Abstração (outro pilar da POO)
# esse conceito da abstração está relacionado com a utilização dessa classe 
# ele quer que você use a sub classe, não a super, e por isso tem o raise
# error
# Se eu estou criando uma classe eu estou criando meu próprio tipo
from pathlib import Path #sus

LOG_FILE = Path(__file__).parent / 'log.txt'

class Log: #Classe mãe, super classe
    def _log(self, msg):
        raise NotImplementedError("Implemente o método log")
    #template method (padrão de projeto)

    def log_error(self, msg):
        return self._log(f'Error: {msg}')
    def log_success(self, msg):
        return self._log(f'Success: {msg}')


class LogFileMixin(Log): #Mixin, adicionar funcionalidades na sua herança múltipla
    def _log(self, msg):
        msg_formatada = f'{msg} ({self.__class__.__name__})'
        print('Salvando no log')
        with open(LOG_FILE, 'a') as arquivo:
            arquivo.write(msg_formatada, '\n')
        print(msg)
    
class LogPrintMixin(Log):
    def _log(self, msg):
        print(f'{msg} ({self.__class__.__name__})')
    



if __name__ == "__main__":
    lp = LogPrintMixin()
    lp.log_error('Qualquer coisa')
    lp.log_success('Deu certo')

    lf = LogFileMixin()
    lf.log_error('Qualquer coisa')
    lf.log_success('Deu certo')
    