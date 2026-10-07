from typing import List
from modelos.pagamento import Pagamento
from persistencia.base_persistencia import BasePersistencia


class PagamentoPersistencia(BasePersistencia):
    """Gerencia a persistência de objetos Pagamento em formato JSON."""

    def __init__(self, caminho: str = "dados/pagamentos.json") -> None:
        super().__init__(caminho)

    def carregar_todos(self) -> List[Pagamento]:
        """Lê o arquivo JSON e reconstrói as instâncias de Pagamento."""
        dados = self.carregar()
        return [Pagamento.from_dict(item) for item in dados]

    def salvar_todos(self, pagamentos: List[Pagamento]) -> None:
        """Salva a lista de pagamentos convertendo cada objeto em dicionário."""
        self.salvar([p.to_dict() for p in pagamentos])