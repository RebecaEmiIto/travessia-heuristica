from enum import Enum
from dataclasses import dataclass

class AcoesJogador(Enum):
    Selecionar_Indivíduo = 'SelecionarIndividuo'

class Individuo(Enum):
    Ovelha = 'Ovelha'
    Repolho = 'Repolho'
    Lobo = 'Lobo'
    
@dataclass  
class AcaoJogador():
    tipo: int
    parametros: int = int() 

    @classmethod
    def SelecionarIndividuo(cls, p1: Individuo) -> 'AcaoJogador':
        return cls(AcoesJogador.Selecionar_Indivíduo, (p1))