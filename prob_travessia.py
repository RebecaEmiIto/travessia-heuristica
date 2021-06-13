import random
from dataclasses import dataclass
from typing import List, Tuple, Iterable
from itertools import islice
from agentes.problemas.travessia import ProblemaTravessia, EstadoTravessia
from regras_jogo.regras_travessia import RegrasTravessia
from percepcoes import PercepcoesJogador

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
    def is_objetivo(self) -> bool:
    #    ordem = prob_travessia.create_ordem_aleatora(1)
    #    for i in ordem:
    #        print(i.tabuleiro)
    #        ProblemaTravessia.acoes(i.tabuleiro)
        return 1#ProblemaTravessia.teste_objetivo(ordem)
        
    
    @property
    def avaliacao(self) -> int:
        """A função de avaliação nos retorna uma pontuação de qualidade
        do atual estado em relação ao objetivo. O objetivo tem necessariamente
        pontuação zero, e quanto maior, pior a avaliação.
        """
        t1 = EstadoTravessia.tabuleiro
        for i in t1:
            print(i)
        return 1#sum(1 for _ in self.num_jogadas)

    @property
    def fitness(self) -> int:
        """Fitness é o complemento de avaliação, e vice-versa."""
        total = sum(n for n in range(self.num_jogadas))
        return total - self.avaliacao

# Testes unitários de programador preguiçoso

#solucao1 = prob_travessia([1,0,3,1,2,0,1])
#assert solucao1.is_objetivo == True
#assert solucao1.avaliacao == 0

def tabuleiro(self):
    tab = RegrasTravessia.tabuleiro(self)
    return tab

def teste(tabuleiro):
    t1 = tabuleiro['Esquerda']
    print(len(t1))

if __name__ == '__main__':
    tabuleiro()