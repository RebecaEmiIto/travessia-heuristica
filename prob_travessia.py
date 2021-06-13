import random
from dataclasses import dataclass
from typing import List, Tuple, Iterable
from itertools import islice
from agentes.problemas.travessia import ProblemaTravessia, EstadoTravessia
from percepcoes import PercepcoesJogador
from regras_jogo.regras_travessia import RegrasTravessia

@dataclass
class prob_travessia:
    tabuleiro: List[int]

    @classmethod
    def create_ordem_aleatoria(cls, qtde, personagens=7, seed=None) -> list:
        return [n for n in islice(cls.ordem_aleatoria(personagens, seed), qtde)]

    @staticmethod
    def ordem_aleatoria(personagens=7, seed=None) -> list:
        random.seed(seed)
        while True:
            yield prob_travessia([random.randint(0,3) for _ in range(7)])
    
    @property
    def is_objetivo(lista) -> bool:
        obj1 = [1,0,3,1,2,0,1]
        obj2 = [1,0,2,1,3,0,1]
        if lista == obj1 or lista == obj2:
            return True
        else:
            return False
    
    @staticmethod
    def avaliacao(percepcao_mundo: PercepcoesJogador) -> int:
        tamanho = len(percepcao_mundo.personagens_esquerda)
        return tamanho

    @staticmethod
    def fitness() -> int:
        """Fitness é o complemento de avaliação, e vice-versa."""
        a = RegrasTravessia()
        instance_variables = vars(a)
        tab = (instance_variables['t1'])
        esquerda = tab['Esquerda']
        resultado = (len(esquerda)) - 3
        return resultado
