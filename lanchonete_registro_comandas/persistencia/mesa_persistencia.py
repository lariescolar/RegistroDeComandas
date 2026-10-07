from typing import List
from modelos.mesa import Mesa
from persistencia.base_persistencia import BasePersistencia


class MesaPersistencia(BasePersistencia):
    """Gerencia a persistência de objetos Mesa em formato JSON."""

    def __init__(self, caminho: str = "dados/mesas.json") -> None:
        super().__init__(caminho)

    def carregar_todas(self) -> List[Mesa]:
        """Lê o arquivo JSON e carrega todas as mesas cadastradas."""
        dados = self.carregar()
        return [Mesa.from_dict(item) for item in dados]

    def salvar_todas(self, mesas: List[Mesa]) -> None:
        """Salva a lista de mesas convertendo cada objeto em dicionário."""
        self.salvar([m.to_dict() for m in mesas])