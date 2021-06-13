from .humano import AgentePrepostoESHumano
from agentes.maquina import Maquina
from agentes.busca_gulosa import BuscaGulosa
from agentes.a_estrela import A_Estrela
from .tipos import TiposAgentes

def construir_agente(*args, **kwargs):
    """ Método factory para uma instância Agente arbitrária, de acordo com os
    paraâmetros. Pode-se mudar à vontade a assinatura do método.
    """
    tipo_agente = args[0]
    if tipo_agente == TiposAgentes.PREPOSTO_HUMANO:
        return AgentePrepostoESHumano()
    elif tipo_agente == TiposAgentes.MAQUINA:
        return Maquina()
    elif tipo_agente == TiposAgentes.A_ESTRELA:
        return A_Estrela()
    elif tipo_agente == TiposAgentes.BUSCA_GULOSA:
        return BuscaGulosa()

    raise ValueError("Agente selecionado não encontrado.")