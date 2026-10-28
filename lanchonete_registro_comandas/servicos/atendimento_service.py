"""Serviços relacionados aos atendimentos."""

from sqlalchemy import select
from sqlalchemy.orm import Session

from excecoes.lanchonete_error import (
    AtendimentoNaoEncontradoError,
    MesaBloqueadaError,
    MesaOcupadaError,
)
from modelos.atendimento import Atendimento
from modelos.mesa import Mesa


class AtendimentoService:
    """Coordena as operações relacionadas aos atendimentos."""

    def __init__(self, sessao: Session) -> None:
        self.__sessao = sessao

    def abrir_atendimento(self, mesa: Mesa) -> Atendimento:
        """Abre um novo atendimento para a mesa informada."""
        if mesa.bloqueada:
            raise MesaBloqueadaError(
                "Não é possível abrir uma comanda em uma mesa bloqueada."
            )

        if mesa.ocupada:
            raise MesaOcupadaError(
                "A mesa já possui um atendimento em andamento."
            )

        atendimento = Atendimento(mesa=mesa)

        try:
            self.__sessao.add(atendimento)
            self.__sessao.commit()
            self.__sessao.refresh(atendimento)
        except Exception:
            self.__sessao.rollback()
            raise

        return atendimento

    def localizar_atendimento(self, mesa: Mesa) -> Atendimento:
        """Localiza o atendimento em aberto (sem data de encerramento) da mesa."""
        comando = select(Atendimento).where(
            Atendimento.mesa_numero == mesa.numero,
            Atendimento.data_encerramento.is_(None),
        )

        atendimento = self.__sessao.scalars(comando).first()

        if atendimento is None:
            raise AtendimentoNaoEncontradoError(
                "Não existe atendimento aberto para essa mesa."
            )

        return atendimento

    def encerrar_atendimento(self, atendimento: Atendimento) -> None:
        """Encerra um atendimento, se ele estiver quitado."""
        try:
            atendimento.encerrar()
            self.__sessao.commit()
            self.__sessao.refresh(atendimento)
        except Exception:
            self.__sessao.rollback()
            raise

    def consultar_historico(self) -> list[Atendimento]:
        """Retorna todos os atendimentos registrados."""
        comando = select(Atendimento).order_by(Atendimento.id)
        return list(self.__sessao.scalars(comando).all())

    def total_geral_atendimentos(self) -> float:
        """Valor total de todos os atendimentos registrados (abertos e encerrados)."""
        return round(sum(a.total for a in self.consultar_historico()), 2)

    def total_geral_pagamentos(self) -> float:
        """Valor total de todos os pagamentos registrados."""
        return round(sum(a.total_pago for a in self.consultar_historico()), 2)
