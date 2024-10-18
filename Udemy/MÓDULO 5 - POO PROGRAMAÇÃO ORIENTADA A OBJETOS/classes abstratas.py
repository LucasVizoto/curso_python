# Classes abstratas - Abstract Base Class(abc)

# ABCs são usadas como contratos para a definição de novas classes.
# Elas podem forçar outras classes a criarem métodos concretos. Também
# podem ter métodos concretos por elas mesmas.
# @abstractmethods são métodos que não tem corpo. 
# As regras para classes abstratas com métodos abstratos é que 
# elas NÃO PODEM  ser instanciadas diretamente.

# Métodos abstratos DEVEM ser implementados nas subclasses (@abstractmethod)
# Uma Classe abstrata em Python tem sua metaclasse sendo ABCMeta.
# (metaclasses são classe em python usadas para criar novas classes )

# É possivel criar @property @setter @classmethod @staticmethod e @method
# como abstratos, para isso use @abstractmethod como decorator mais interno.

from abc import ABC, ABCMeta, abstractmethod
#essa classe tem unicamente o objetivo de receber como herança a metaclass ABCMeta


class Log_exemplo(metaclass = ABCMeta):
    ...
#é a msm coisa
class Log(ABC): #Classe mãe, super classe
    @abstractmethod
    def _log(self, msg): ... 
# virou uma classe abstrata
#Uma classe abstrata não deve ser instanciada

    def log_error(self, msg):
        return self._log(f'Error: {msg}')
    def log_success(self, msg):
        return self._log(f'Success: {msg}')
    
class LogPrintMixin(Log):
    def _log(self, msg):
        print(f'{msg} ({self.__class__.__name__})')

l = LogPrintMixin()
l.log_error('OI')