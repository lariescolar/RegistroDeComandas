"""Pacote responsável pela camada de persistência em arquivos JSON."""

from .base_persistencia import BasePersistencia
from .produto_persistencia import ProdutoPersistencia
from .mesa_persistencia import MesaPersistencia
from .pedido_persistencia import PedidoPersistencia
from .pagamento_persistencia import PagamentoPersistencia
from .atendimento_persistencia import AtendimentoPersistencia

__all__ = [
    "BasePersistencia",
    "ProdutoPersistencia",
    "MesaPersistencia",
    "PedidoPersistencia",
    "PagamentoPersistencia",
    "AtendimentoPersistencia",
]