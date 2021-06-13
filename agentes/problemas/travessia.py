from typing import Sequence, Set
from dataclasses import dataclass

@dataclass
class Personagens:
    p1: int

    def __hash__(self) -> int:
        return hash(self.p1) + hash(self.p2)
    
    def __str__(self) -> str:
        return f'Pessoa 1: ({self.p1} || Pessoa 2: {self.p1})'

@dataclass
class EstadoTravessia:
    tabuleiro: [Personagens]

@dataclass
class Mover:
    personagens: Personagens

    def __str__(self) -> str:
        return f'Mover {self.personagens} para o outro lado do Rio'

class ProblemaTravessia:
    @staticmethod
    def estado_inicial():
        nivel = {
            'Esquerda': [1,2,3],
            'Direita': []
            }
        return nivel
    
    @staticmethod
    def acoes(estado: EstadoTravessia) -> Sequence[Mover]:
        acoes_possiveis = list()
        for individuo1 in estado:
            for individuo2 in estado:
                direita = estado['Direita']
                esquerda = estado['Esquerda']
                if individuo1 in esquerda:
                    pessoa1 = esquerda.p1
                    if Personagens(pessoa1) in esquerda:
                        acoes_possiveis.append(Mover(individuo1))
                        
                if individuo1 in direita:
                    if Personagens(pessoa1) in direita:
                        acoes_possiveis.append(Mover(individuo1))

        return acoes_possiveis
    
    @staticmethod
    def resultado(estado: EstadoTravessia, acao: Mover) -> EstadoTravessia:
        estado_resultante = EstadoTravessia(set(estado))
        direita = estado['Direita']
        esquerda = estado['Esquerda']
        contador = 0
        if contador % 2 == 0: # Jangada na esquerda
            for i in range(len(esquerda)):
                p1 = acao.estado['Esquerda'][i]
                print(estado_resultante.tabuleiro['Direita'])
                estado_resultante['Direita'].add(p1)
                
                if (p1 in estado_resultante['Esquerda']):
                    estado_resultante['Esquerda'].remove(p1)
                    estado_resultante['Direita'].insert(0, p1)
                    
                    if EstadoTravessia.ValidacaoEsquerda() is True and ValidacaoDireita() is True:
                        contador += 1
                    else:
                        estado_resultante['Direita'].remove(p1)
                        estado_resultante['Esquerda'].insert(0, p1)
                        raise ValueError("Movimento especificado inválido, cheater!")
                raise ValueError("Personagem {p1} nã encontrado na Esquerda")

        else: # Jangada na Direita
            for i in range(len(direita)):
                p1 = acao.estado['Direita'][i]
                print(estado_resultante.tabuleiro['Esquerda'])
                estado_resultante['Esquerda'].add(p1)
                
                if (p1 in estado_resultante['Direita']):
                    estado_resultante['Direita'].remove(p1)
                    estado_resultante['Esquerda'].insert(0, p1)
                    
                    if EstadoTravessia.ValidacaoEsquerda() is True and ValidacaoDireita() is True:
                        contador += 1
                    else:
                        estado_resultante['Esquerda'].remove(p1)
                        estado_resultante['Direita'].insert(0, p1)
                        raise ValueError("Movimento especificado inválido, cheater!")
                raise ValueError("Personagem {p1} nã encontrado na Direita")
        print(f'estado resultante tabu = {estado_resultante}')
        return estado_resultante
    
    def ValidacaoEsquerda(self) -> bool:
        tabuleiro = self.t1
        esquerda = tabuleiro['Esquerda']
        if 'Ovelha' in esquerda:
            if 'Repolho' in esquerda and 'Lobo' not in esquerda:
                return False
            else:
                return True

        if 'Lobo' in esquerda:
            if ('Ovelha' in esquerda):
                return False
            else:
                return True

    def ValidacaoDireita(self) -> bool:
        tabuleiro = self.t1
        direita = tabuleiro['Direita']
        # Lado Direito
        if 'Ovelha' in direita:
            if 'Repolho' in direita and 'Lobo' not in direita:
                return False
            else:
                return True

        if 'Lobo' in direita:
            if ('Ovelha' in direita):
                return False
            else:
                return True

    @staticmethod
    def teste_objetivo(estado: EstadoTravessia) -> bool:
        esquerda = estado['Esquerda']
        print(f'tamanho = {len(esquerda)}')
        if len(esquerda) == 0:
            return True
        else:
            return False
    
    @staticmethod
    def custo(inicial: EstadoTravessia, acao: Mover,
              resultante: EstadoTravessia) -> int:
        """Custo em quantidade de jogadas"""
        return 1
