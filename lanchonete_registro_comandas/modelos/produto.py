from abc import ABC, abstractmethod


class Produto(ABC):
    """
    Representa um produto comercializado pela lanchonete.
    Classe base para os diferentes tipos de produtos.
    """

    def __init__(
        self,
        codigo: int,
        nome: str,
        preco: float,
        disponivel: bool = True
    ) -> None:
        """
        Inicializa um produto.

        Args:
            codigo: Código de identificação do produto.
            nome: Nome do produto.
            preco: Preço do produto.
            disponivel: Indica se o produto está disponível para venda.
        """
        self.__codigo: int = codigo
        self.__nome: str = nome
        self.__preco: float = preco
        self.__disponivel: bool = disponivel

    @property
    def codigo(self) -> int:
        """Retorna o código do produto."""
        return self.__codigo

    @property
    def nome(self) -> str:
        """Retorna o nome do produto."""
        return self.__nome

    @property
    def preco(self) -> float:
        """Retorna o preço do produto."""
        return self.__preco

    @property
    def disponivel(self) -> bool:
        """Retorna a disponibilidade do produto."""
        return self.__disponivel

    def alterar_disponibilidade(self, disponivel: bool) -> None:
        """
        Altera a disponibilidade do produto.

        Args:
            disponivel: Nova situação de disponibilidade do produto.
        """
        self.__disponivel = disponivel

    @abstractmethod
    def descricao(self) -> str:
        """
        Retorna uma descrição específica do tipo de produto.

        Este método deverá ser implementado pelas subclasses.
        """
        pass

    def __str__(self) -> str:
        status = "Disponível" if self.__disponivel else "Indisponível"
        return (
            f"{self.descricao()} | Código: {self.__codigo} | "
            f"R$ {self.__preco:.2f} | {status}"
        )


class Suco(Produto):
    """Representa um suco vendido pela lanchonete."""

    def descricao(self) -> str:
        """Retorna a descrição do suco."""
        return f"Suco: {self.nome}"


class Sanduiche(Produto):
    """Representa um sanduíche vendido pela lanchonete."""

    def descricao(self) -> str:
        """Retorna a descrição do sanduíche."""
        return f"Sanduíche: {self.nome}"
