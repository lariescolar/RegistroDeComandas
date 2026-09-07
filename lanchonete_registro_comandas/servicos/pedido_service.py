"""Serviços relacionados aos pedidos."""

from __future__ import annotations

from modelos.atendimento import Atendimento
from modelos.pedido import Pedido
from modelos.produto import Produto


class PedidoService:
    """Coordena o registro de pedidos em um atendimento."""

    def registrar_pedido(
        self,
        atendimento: Atendimento,
        produto: Produto,
        quantidade: int,
    ) -> Pedido:
        """Cria e adiciona um pedido ao atendimento."""
        pedido = Pedido(produto, quantidade)
        atendimento.adicionar_pedido(pedido)
        return pedido
