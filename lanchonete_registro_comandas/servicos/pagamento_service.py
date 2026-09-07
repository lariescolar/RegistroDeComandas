"""Serviços relacionados aos pagamentos."""

from __future__ import annotations

from modelos.atendimento import Atendimento
from modelos.pagamento import Pagamento


class PagamentoService:
    """Coordena o registro de pagamentos em um atendimento."""

    def registrar_pagamento(self, atendimento: Atendimento, valor: float) -> Pagamento:
        """Cria e adiciona um pagamento ao atendimento."""
        pagamento = Pagamento(valor)
        atendimento.registrar_pagamento(pagamento)
        return pagamento
