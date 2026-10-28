import math
from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import DateTime, ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from formatacao import formatar_moeda
from modelos.base import Base
from excecoes.lanchonete_error import (
    AtendimentoEncerradoError,
    AtendimentoNaoQuitadoError,
    PagamentoInvalidoError,
)

if TYPE_CHECKING:
    from modelos.mesa import Mesa
    from modelos.pedido import Pedido
    from modelos.pagamento import Pagamento


class Atendimento(Base):
    """Representa um atendimento de uma mesa,
    contendo pedidos e pagamentos."""

    __tablename__ = "atendimentos"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True
    )

    mesa_numero: Mapped[int] = mapped_column(
        ForeignKey("mesas.numero")
    )

    # Preenchida automaticamente pelo banco de dados na inserção.
    data_abertura: Mapped[datetime] = mapped_column(
        DateTime,
        server_default=func.now()
    )

    # None (NULL no banco) significa que o atendimento está em aberto.
    data_encerramento: Mapped[datetime | None] = mapped_column(
        DateTime,
        nullable=True,
        default=None
    )

    mesa: Mapped["Mesa"] = relationship(
        back_populates="atendimentos"
    )

    pedidos: Mapped[list["Pedido"]] = relationship(
        back_populates="atendimento",
        cascade="all, delete-orphan"
    )

    pagamentos: Mapped[list["Pagamento"]] = relationship(
        back_populates="atendimento",
        cascade="all, delete-orphan"
    )

    @property
    def encerrado(self) -> bool:
        return self.data_encerramento is not None

    @property
    def total(self) -> float:
        """Soma dos valores dos pedidos, arredondada em centavos."""
        return round(sum(pedido.valor for pedido in self.pedidos), 2)

    @property
    def total_pago(self) -> float:
        """Soma dos valores dos pagamentos, arredondada em centavos."""
        return round(sum(pg.valor for pg in self.pagamentos), 2)

    @property
    def saldo(self) -> float:
        """Total menos o total pago, arredondado em centavos.

        O arredondamento evita que erros de ponto flutuante (ex.: 5.5e-17)
        sejam interpretados como saldo pendente.
        """
        return round(self.total - self.total_pago, 2)

    def adicionar_pedido(self, pedido: "Pedido") -> None:
        if self.encerrado:
            raise AtendimentoEncerradoError(
                "Não é possível adicionar pedidos a um atendimento encerrado."
            )

        self.pedidos.append(pedido)

    def registrar_pagamento(self, pagamento: "Pagamento") -> None:
        if self.encerrado:
            raise AtendimentoEncerradoError(
                "Não é possível registrar pagamentos em um atendimento encerrado."
            )

        if not math.isfinite(pagamento.valor) or pagamento.valor <= 0:
            raise PagamentoInvalidoError(
                "O valor do pagamento deve ser maior que zero."
            )

        if round(pagamento.valor, 2) > self.saldo:
            raise PagamentoInvalidoError(
                "O pagamento não pode ser superior ao saldo da comanda."
            )

        self.pagamentos.append(pagamento)

    def encerrar(self) -> None:
        if self.encerrado:
            raise AtendimentoEncerradoError(
                "O atendimento já está encerrado."
            )

        if self.saldo > 0:
            raise AtendimentoNaoQuitadoError(
                "Não é possível encerrar um atendimento com saldo pendente."
            )

        # A data/hora é gerada pelo banco, como em data_abertura.
        # A mesa volta a ficar livre automaticamente (Mesa.ocupada é calculada).
        self.data_encerramento = func.now()

    def __str__(self) -> str:
        status = "Encerrado" if self.encerrado else "Em aberto"
        situacao_mesa = "Bloqueada" if self.mesa.bloqueada else "Desbloqueada"
        abertura = (
            self.data_abertura.strftime("%d/%m/%Y %H:%M")
            if self.data_abertura is not None
            else "-"
        )
        return (
            f"Atendimento #{self.id} | Mesa {self.mesa.numero} ({situacao_mesa}) | "
            f"{status} | Aberto em {abertura} | "
            f"Total: {formatar_moeda(self.total)} | "
            f"Pago: {formatar_moeda(self.total_pago)} | "
            f"Saldo: {formatar_moeda(self.saldo)}"
        )
