import sys
from typing import Set, Tuple
from .regras_abstratas import AbstractRegrasJogo
from .personagens import Personagens
from percepcoes import PercepcoesJogador
from acoes import AcoesJogador, Individuo

sys.path.append("..")

class RegrasTravessia(AbstractRegrasJogo):
    def __init__(self) -> None:
        super().__init__()
        t0 = {'Esquerda': ['Ovelha', 'Repolho', 'Lobo'],
              'Direita': []}
        self.jogadas = 0
        self.t1 = t0
        self.cont = 0
        self.id_personagem = {Personagens.O_JOGADOR: 0}
        self.acao_personagem = {0: None}
        self.msg_jogador = None

    def registrarAgentePersonagem(self, personagem:list):
        """ Cria ou recupera id de um personagem agente.
        """
        return self.id_personagem[personagem]

    def isFim(self):
        return len(self.t1["Direita"]) == 3

    def gerarCampoVisao(self, id_agente):
        """ Retorna um EstadoJogoView para ser consumido por um agente
        específico. Objeto deve conter apenas descrição de elementos visíveis
        para este agente.

        EstadoJogoView é um objeto imutável ou uma cópia do jogo, de forma que
        sua manipulação direta não tem nenhum efeito no mundo de jogo real.
        """
        percepcoes_jogador = PercepcoesJogador(
            personagens_esquerda = set(self.t1['Esquerda']),
            personagens_direita = set(self.t1['Direita']),
            mensagem_jogo = self.msg_jogador)

        self.msg_jogador = None
        return percepcoes_jogador
        

    def registrarProximaAcao(self, id_agente, acao):
        """ Informa ao jogo qual a ação de um jogador especificamente.
        Neste momento, o jogo ainda não é transformado em seu próximo estado,
        isso é feito no método de atualização do mundo.
        """
        self.acao_personagem[id_agente] = acao

    def atualizarEstado(self, diferencial_tempo):
        """ Apenas neste momento o jogo é atualizado para seu próximo estado
        de acordo com as ações de cada jogador registradas anteriormente.
        """
        self.jogadas += 1
        acao_jogador = self.acao_personagem[
            self.id_personagem[Personagens.O_JOGADOR]]
        if acao_jogador.tipo == AcoesJogador.Selecionar_Indivíduo:
            p1 = acao_jogador.parametros
            # Devolve o valor(personagem) de cada integer
            pessoa1 = self.decodificar_pessoa(p1)

            if self.cont % 2 == 0: # Jangada na esquerda
                # Seleção da Esquerda
                if (pessoa1 in self.t1['Esquerda']):
                    self.t1['Esquerda'].remove(pessoa1)
                    self.t1['Direita'].insert(0, pessoa1)
                    
                    # Confere se a jogada é valida
                    if self.ValidacaoEsquerda() is True and self.ValidacaoDireita() is True:
                        self.cont += 1
                    else:
                        self.t1['Direita'].remove(pessoa1)
                        self.t1['Esquerda'].insert(0, pessoa1)
                        self.msg_jogador = f'Movimento inválido.'
                elif pessoa1 == None:
                    if self.ValidacaoEsquerda() is True and self.ValidacaoDireita() is True:
                        self.cont += 1
                else:
                    self.msg_jogador = f'{pessoa1} não encontrado.'
            
            else: # Jangada na direita
                # Seleção da Direita
                if (pessoa1 in self.t1['Direita']):
                    self.t1['Direita'].remove(pessoa1)
                    self.t1['Esquerda'].insert(0, pessoa1)

                    # Confere se a jogada é valida
                    if self.ValidacaoEsquerda() is True and self.ValidacaoDireita() is True:
                        self.cont += 1
                    else:
                        self.t1['Esquerda'].remove(pessoa1)
                        self.t1['Direita'].insert(0, pessoa1)
                        self.msg_jogador = f'Movimento inválido.'
                elif pessoa1 == None:
                    if self.ValidacaoEsquerda() is True and self.ValidacaoDireita() is True:
                        self.cont += 1
                else:
                    self.msg_jogador = f'{pessoa1} não encontrado.'
        
        return self.t1

    def terminarJogo(self):
        """ Faz procedimentos de fim de jogo, como mostrar placar final,
        gravar resultados, etc...
        """
        return

    def ValidacaoDireita(self) -> bool:
        """Mais informações sobre as regras no arquivo README.md"""
        tabuleiro = self.t1
        direita = tabuleiro['Direita']
        if len(direita) > 1:
            if 'Ovelha' in direita and 'Repolho' in direita:
                if ('Lobo' in direita or (self.cont+1)%2 == 1):
                    return True
            else:
                return True

            if 'Lobo' in direita and 'Ovelha' in direita:
                if ('Repolho' in direita or (self.cont+1)%2 == 1):
                    return True
            else:
                return True
        else:
            return True
        return False

    def ValidacaoEsquerda(self) -> bool:
        """Mais informações sobre as regras no arquivo README.md"""
        tabuleiro = self.t1
        # Lado Esquerdo
        print(self.cont)
        esquerda = tabuleiro['Esquerda']
        if len(esquerda) > 1:    
            if 'Ovelha' in esquerda and 'Repolho' in esquerda: 
                if ('Lobo' in esquerda or (self.cont+1)%2 == 0):
                    return True
            else:
                return True

            if 'Lobo' in esquerda and 'Ovelha' in esquerda:
                if ('Repolho' in esquerda or (self.cont+1)%2 == 0):
                    return True
            else:
                return True

        else:
            return True
        return False
    
    def avaliacao():
        direita = RegrasTravessia.ValidacaoDireita
        esquerda = RegrasTravessia.ValidacaoEsquerda
        if esquerda is True and direita is True:
            return True
        else:
            return False

    @staticmethod
    def decodificar_pessoa(p):
        pessoa = p
        if pessoa == 1:
            return 'Ovelha'
        elif pessoa == 2:
            return 'Repolho'
        elif pessoa == 3:
            return 'Lobo'
        else:
            return None
            

def construir_jogo(*args, **kwargs):
    """ Método factory para uma instância RegrasJogo arbitrária, de acordo com os
    parâmetros. Pode-se mudar à vontade a assinatura do método.
    """
    return RegrasTravessia()