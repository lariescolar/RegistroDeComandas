"""Serviços relacionados aos pagamentos."""

from sqlalchemy.orm import Session

from modelos.atendimento import Atendimento
from modelos.pagamento import Pagamento


class PagamentoService:
    """Coordena o registro de pagamentos em um atendimento."""

    def __init__(self, sessao: Session) -> None:
        self.__sessao = sessao

    def registrar_pagamento(self, atendimento: Atendimento, valor: float) -> Pagamento:
        """Cria e adiciona um pagamento ao atendimento."""
        pagamento = Pagamento(valor=valor)

        try:
            atendimento.registrar_pagamento(pagamento)
            self.__sessao.commit()
            self.__sessao.refresh(pagamento)
        except Exception:
            self.__sessao.rollback()
            raise

        return pagamento
