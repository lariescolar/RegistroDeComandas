from typing import List, Dict
from modelos.pedido import Pedido
from modelos.produto import Produto
from persistencia.base_persistencia import BasePersistencia
from excecoes.lanchonete_error import RelacionamentoInvalidoError


class PedidoPersistencia(BasePersistencia):
    """Gerencia a persistência de objetos Pedido em formato JSON."""

    def __init__(self, caminho: str = "dados/pedidos.json") -> None:
        super().__init__(caminho)

    def carregar_todos(self, produtos: List[Produto]) -> List[Pedido]:
        """
        Lê o arquivo de pedidos e reconstrói a associação com Produto.
        """
        dados = self.carregar()
        mapa_produtos: Dict[int, Produto] = {p.codigo: p for p in produtos}

        pedidos: List[Pedido] = []
        for item in dados:
            cod_prod = item.get("codigo_produto")
            if cod_prod not in mapa_produtos:
                raise RelacionamentoInvalidoError(
                    f"Produto com código #{cod_prod} referenciado no Pedido #{item.get('id')} não existe."
                )

            prod_obj = mapa_produtos[cod_prod]
            pedido = Pedido.from_dict(item, produto=prod_obj)
            pedidos.append(pedido)

        return pedidos

    def salvar_todos(self, pedidos: List[Pedido]) -> None:
        """Salva a lista de pedidos convertendo cada objeto em dicionário."""
        self.salvar([p.to_dict() for p in pedidos])