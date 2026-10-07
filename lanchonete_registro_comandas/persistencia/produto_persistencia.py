from typing import List
from modelos.produto import Produto
from persistencia.base_persistencia import BasePersistencia


class ProdutoPersistencia(BasePersistencia):
    """Gerencia a persistência de objetos Produto em formato JSON."""

    def __init__(self, caminho: str = "dados/produtos.json") -> None:
        super().__init__(caminho)

    def carregar_todos(self) -> List[Produto]:
        """Lê o arquivo JSON e reconstrói as instâncias concretas de Produto."""
        dados = self.carregar()
        return [Produto.from_dict(item) for item in dados]

    def salvar_todos(self, produtos: List[Produto]) -> None:
        """Salva a lista de produtos convertendo cada objeto em dicionário."""
        self.salvar([p.to_dict() for p in produtos])