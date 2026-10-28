"""Serviços relacionados aos pedidos."""

from sqlalchemy.orm import Session

from excecoes.lanchonete_error import ProdutoIndisponivelError
from modelos.atendimento import Atendimento
from modelos.pedido import Pedido
from modelos.produto import Produto


class PedidoService:
    """Coordena o registro de pedidos em um atendimento."""

    def __init__(self, sessao: Session) -> None:
        self.__sessao = sessao

    def registrar_pedido(
        self,
        atendimento: Atendimento,
        produto: Produto,
        quantidade: int,
    ) -> Pedido:
        """Cria e adiciona um pedido ao atendimento."""
        if not produto.disponivel:
            raise ProdutoIndisponivelError("Esse produto está indisponível.")

        # "quantidade" vem primeiro: se for inválida, a exceção é levantada
        # antes de o pedido ser associado ao produto.
        pedido = Pedido(quantidade=quantidade, produto=produto)

        try:
            atendimento.adicionar_pedido(pedido)
            self.__sessao.commit()
            self.__sessao.refresh(pedido)
        except Exception:
            self.__sessao.rollback()
            raise

        return pedido
