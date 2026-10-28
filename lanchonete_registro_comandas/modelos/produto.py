from sqlalchemy import Float, String
from sqlalchemy.orm import Mapped, mapped_column

from formatacao import formatar_moeda
from modelos.base import Base


class Produto(Base):
    """
    Representa um produto comercializado pela lanchonete.

    Classe base (conceitualmente abstrata) dos tipos de produto: não deve
    ser instanciada diretamente, apenas suas subclasses (Suco, Sanduiche).

    Os produtos usam herança de tabela única: todas as subclasses são
    gravadas na tabela "produtos", diferenciadas pela coluna "tipo".
    """

    __tablename__ = "produtos"

    # O código do produto é informado pelo usuário e identifica o produto.
    codigo: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=False
    )

    nome: Mapped[str] = mapped_column(String(100))

    preco: Mapped[float] = mapped_column(Float)

    disponivel: Mapped[bool] = mapped_column(default=True)

    tipo: Mapped[str] = mapped_column(String(30))

    __mapper_args__ = {
        "polymorphic_on": "tipo",
        "polymorphic_identity": "Produto",
    }

    def alterar_disponibilidade(self, disponivel: bool) -> None:
        """Altera a disponibilidade do produto."""
        self.disponivel = disponivel

    def descricao(self) -> str:
        """Retorna a descrição do tipo de produto (implementada nas subclasses)."""
        raise NotImplementedError(
            "As subclasses de Produto devem implementar descricao()."
        )

    def __str__(self) -> str:
        status = "Disponível" if self.disponivel else "Indisponível"
        return (
            f"{self.descricao()} | Código: {self.codigo} | "
            f"{formatar_moeda(self.preco)} | {status}"
        )


class Suco(Produto):
    """Representa um suco vendido pela lanchonete."""

    __mapper_args__ = {"polymorphic_identity": "Suco"}

    def descricao(self) -> str:
        """Retorna a descrição do suco."""
        return f"Suco: {self.nome}"


class Sanduiche(Produto):
    """Representa um sanduíche vendido pela lanchonete."""

    __mapper_args__ = {"polymorphic_identity": "Sanduiche"}

    def descricao(self) -> str:
        """Retorna a descrição do sanduíche."""
        return f"Sanduíche: {self.nome}"
