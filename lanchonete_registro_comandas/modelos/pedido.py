from modelos.produto import Produto
from excecoes.lanchonete_error import QuantidadeInvalidaError


class Pedido:
    """
    Representa um produto solicitado durante um atendimento.
    """

    def __init__(self, produto: Produto, quantidade: int) -> None:
        if quantidade <= 0:
            raise QuantidadeInvalidaError(
                "A quantidade deve ser maior que zero."
            )

        self.__produto: Produto = produto
        self.__quantidade: int = quantidade

    @property
    def produto(self) -> Produto:
        return self.__produto

    @property
    def quantidade(self) -> int:
        return self.__quantidade

    @property
    def valor(self) -> float:
        return self.__produto.preco * self.__quantidade

    def __str__(self) -> str:
        return (
            f"{self.__produto.nome} x {self.__quantidade} - "
            f"R$ {self.valor:.2f}"
        )
