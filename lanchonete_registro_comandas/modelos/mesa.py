from sqlalchemy.orm import Mapped, mapped_column, relationship

from modelos.base import Base
from excecoes.lanchonete_error import (
    MesaJaBloqueadaError,
    MesaJaDesbloqueadaError,
)


class Mesa(Base):
    """Representa uma mesa da lanchonete."""

    __tablename__ = "mesas"

    # O número da mesa é informado pelo usuário e identifica a mesa.
    numero: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=False
    )

    bloqueada: Mapped[bool] = mapped_column(default=False)

    atendimentos: Mapped[list["Atendimento"]] = relationship(
        back_populates="mesa"
    )

    @property
    def ocupada(self) -> bool:
        """Uma mesa está ocupada quando possui um atendimento em aberto.

        O valor é calculado a partir dos atendimentos, e não armazenado.
        """
        return any(not a.encerrado for a in self.atendimentos)

    def bloquear(self) -> None:
        if self.bloqueada:
            raise MesaJaBloqueadaError("A mesa já está bloqueada.")
        self.bloqueada = True

    def desbloquear(self) -> None:
        if not self.bloqueada:
            raise MesaJaDesbloqueadaError("A mesa já está desbloqueada.")
        self.bloqueada = False

    def __str__(self) -> str:
        status_bloqueio = "Bloqueada" if self.bloqueada else "Desbloqueada"
        status_ocupacao = "Ocupada" if self.ocupada else "Livre"
        return f"Mesa {self.numero} - {status_bloqueio} | {status_ocupacao}"
