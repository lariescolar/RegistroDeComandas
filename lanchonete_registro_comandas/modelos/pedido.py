from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship, validates

from formatacao import formatar_moeda
from modelos.base import Base
from excecoes.lanchonete_error import QuantidadeInvalidaError


class Pedido(Base):
    """Representa um produto solicitado durante um atendimento."""

    __tablename__ = "pedidos"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True
    )

    atendimento_id: Mapped[int] = mapped_column(
        ForeignKey("atendimentos.id")
    )

    produto_codigo: Mapped[int] = mapped_column(
        ForeignKey("produtos.codigo")
    )

    quantidade: Mapped[int]

    atendimento: Mapped["Atendimento"] = relationship(
        back_populates="pedidos"
    )

    produto: Mapped["Produto"] = relationship()

    @validates("quantidade")
    def _validar_quantidade(self, chave: str, valor: int) -> int:
        """Regra de negócio: a quantidade deve ser maior que zero."""
        if valor is None or valor <= 0:
            raise QuantidadeInvalidaError(
                "A quantidade deve ser maior que zero."
            )
        return valor

    @property
    def valor(self) -> float:
        return self.produto.preco * self.quantidade

    def __str__(self) -> str:
        return (
            f"{self.produto.nome} x {self.quantidade} - "
            f"{formatar_moeda(self.valor)}"
        )
