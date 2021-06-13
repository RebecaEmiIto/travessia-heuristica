from typing import Tuple
from .abstrato import AgenteAbstrato
from percepcoes import PercepcoesJogador
from acoes import AcaoJogador, Individuo

class AgentePrepostoESHumano(AgenteAbstrato):
    def __init__(self):
        self.count = 0
    
    def adquirirPercepcao(self, percepcao_mundo: PercepcoesJogador):
        """ Inspeciona a disposicao dos elementos no objeto de visao e escreve
        na tela para o usuário saber o que seu agente está percebendo.
        """
        #print(f'Contador = {self.count}')
        print('--- Tabuleiro após a ultima jogada: ---\n')
        print('|[ 1-Ovelha || 2-Repolho || 3-Lobo ]|\n')

        print(percepcao_mundo.personagens_esquerda)

        print('Margem Esquerda'.center(40, '-'))

        if self.count % 2 == 0:
            print('Jangada\n'.center(40, ' '))
        else:
            print('')
            print('Jangada'.center(40, ' '))

        print('Margem Direita'.center(40, '-'))

        print(percepcao_mundo.personagens_direita)
        
        if percepcao_mundo.mensagem_jogo:
            print(f'Mensagem do jogo: {percepcao_mundo.mensagem_jogo}')
            
        else:
            self.count += 1

    def escolherProximaAcao(self):  
        jogada = None
        while not jogada:
            jogada = input('Escreva sua jogada no formato [número]\n').strip()
            if len(jogada) == 1:
                p1 = AgentePrepostoESHumano.parse_jogada(jogada)
            else:
                jogada = None
                print('Jogada entrada é inválida. Tente novamente.')

        return AcaoJogador.SelecionarIndividuo(p1)

    @staticmethod
    def parse_jogada(entrada: str) -> int:
        pessoa = {
            0: 0,
            1: Individuo.Ovelha,
            2: Individuo.Repolho,
            3: Individuo.Lobo
        }
        
        p1 = entrada
        return p1
