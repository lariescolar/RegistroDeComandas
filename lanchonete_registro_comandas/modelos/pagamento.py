from sqlalchemy import Float, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from formatacao import formatar_moeda
from modelos.base import Base


class Pagamento(Base):
    """Representa um pagamento realizado pelo cliente."""

    __tablename__ = "pagamentos"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True
    )

    atendimento_id: Mapped[int] = mapped_column(
        ForeignKey("atendimentos.id")
    )

    valor: Mapped[float] = mapped_column(Float)

    atendimento: Mapped["Atendimento"] = relationship(
        back_populates="pagamentos"
    )

    def __str__(self) -> str:
        return formatar_moeda(self.valor)
