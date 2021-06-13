from .humano import AgentePrepostoESHumano
from agentes.maquina import Maquina
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

    raise ValueError("Agente selecionado não encontrado.")