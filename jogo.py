#!/usr/bin/env python3

import time
from regras_jogo.regras_travessia import construir_jogo
from regras_jogo.personagens import Personagens
from agentes import construir_agente
from agentes.tipos import TiposAgentes
import prob_travessia

def ler_tempo(em_turnos=False):
    """ Se o jogo for em turnos, retorna a passada de 1 rodada.
    
    Se não for em turno, é continuo ou estratégico, retorna tempo
    preciso (ns) do relógio.
    """
    return 1 if em_turnos else time.time()


def iniciar_jogo():
    # Inicializar e configurar jogo
    jogo = construir_jogo()
    personagem_jogador = jogo.registrarAgentePersonagem(Personagens.O_JOGADOR)
    opcao = input('[ 1 - Humano ][ 2 - Maquina ][ 3 - Busca Gulosa ][ 4 - A Estrela ]\n')
    if opcao == 1:
        agente_jogador = construir_agente(TiposAgentes.PREPOSTO_HUMANO, Personagens.O_JOGADOR)
    elif opcao == 2:
        agente_jogador = construir_agente(TiposAgentes.MAQUINA, Personagens.O_JOGADOR)
    elif opcao == 3:
        agente_jogador = construir_agente(TiposAgentes.BUSCA_GULOSA, Personagens.O_JOGADOR)
    elif opcao == 4:
        agente_jogador = construir_agente(TiposAgentes.A_ESTRELA, Personagens.O_JOGADOR)

    tempo_de_jogo = 0
    while not jogo.isFim():
        # Mostrar mundo ao jogador
        ambiente_perceptivel = jogo.gerarCampoVisao(personagem_jogador)
        agente_jogador.adquirirPercepcao(ambiente_perceptivel)
        # Decidir jogada e apresentar ao jogo
        if opcao == 2:
            personagem = prob_travessia.prob_travessia.create_ordem_aleatoria(1)
            for i in personagem:
                for j in i.tabuleiro:
                    #print(j)
                    acao = agente_jogador.escolherProximaAcao(j)
                    jogo.registrarProximaAcao(personagem_jogador, acao)
                    tempo_corrente = ler_tempo()

                    novoCampo = jogo.atualizarEstado(tempo_corrente - tempo_de_jogo)
                    tempo_de_jogo += tempo_corrente
                    
                    ambiente_perceptivel = jogo.gerarCampoVisao(personagem_jogador)
                    agente_jogador.adquirirPercepcao(ambiente_perceptivel)
            
        else:
            acao = agente_jogador.escolherProximaAcao()
            jogo.registrarProximaAcao(personagem_jogador, acao)
            #Atualizar jogo
            tempo_corrente = ler_tempo()
            jogo.atualizarEstado(tempo_corrente - tempo_de_jogo)
            tempo_de_jogo += tempo_corrente


if __name__ == '__main__':
    iniciar_jogo()