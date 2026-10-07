from modelos.produto import Produto
from excecoes.lanchonete_error import QuantidadeInvalidaError


class Pedido:
    """
    Representa um produto solicitado durante um atendimento.
    """

    def __init__(
        self,
        produto: Produto,
        quantidade: int,
        id_pedido: int | None = None
    ) -> None:
        if quantidade <= 0:
            raise QuantidadeInvalidaError(
                "A quantidade deve ser maior que zero."
            )

        self.__id: int | None = id_pedido
        self.__produto: Produto = produto
        self.__quantidade: int = quantidade

    @property
    def id(self) -> int | None:
        return self.__id

    @property
    def produto(self) -> Produto:
        return self.__produto

    @property
    def quantidade(self) -> int:
        return self.__quantidade

    @property
    def valor(self) -> float:
        return self.__produto.preco * self.__quantidade

    def to_dict(self) -> dict:
        codigo_produto = getattr(
            self.__produto,
            "codigo",
            getattr(self.__produto, "id", None)
        )
        return {
            "id": self.__id,
            "codigo_produto": codigo_produto,
            "quantidade": self.__quantidade,
        }

    @classmethod
    def from_dict(cls, dados: dict, produto: Produto) -> "Pedido":
        return cls(
            produto=produto,
            quantidade=int(dados["quantidade"]),
            id_pedido=dados.get("id"),
        )

    def __str__(self) -> str:
        return (
            f"{self.__produto.nome} x {self.__quantidade} - "
            f"R$ {self.valor:.2f}"
        )