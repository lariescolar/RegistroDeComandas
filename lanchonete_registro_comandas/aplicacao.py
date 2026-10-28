"""Camada de aplicação da lanchonete.

Controla o ciclo de vida da sessão do SQLAlchemy e disponibiliza os serviços
(todos compartilham a mesma sessão) para a interface.
"""

from sqlalchemy.orm import Session

from persistencia.banco import criar_sessao, criar_tabelas
from servicos.atendimento_service import AtendimentoService
from servicos.mesa_service import MesaService
from servicos.pagamento_service import PagamentoService
from servicos.pedido_service import PedidoService
from servicos.produto_service import ProdutoService


class Aplicacao:
    """Inicializa o banco, abre a sessão e expõe os serviços."""

    def __init__(self) -> None:
        criar_tabelas()
        self.__sessao: Session | None = None

        self.__mesa_service: MesaService | None = None
        self.__produto_service: ProdutoService | None = None
        self.__atendimento_service: AtendimentoService | None = None
        self.__pedido_service: PedidoService | None = None
        self.__pagamento_service: PagamentoService | None = None

    def __enter__(self) -> "Aplicacao":
        self.__sessao = criar_sessao()

        self.__mesa_service = MesaService(self.sessao)
        self.__produto_service = ProdutoService(self.sessao)
        self.__atendimento_service = AtendimentoService(self.sessao)
        self.__pedido_service = PedidoService(self.sessao)
        self.__pagamento_service = PagamentoService(self.sessao)

        return self

    def __exit__(self, tipo_excecao, excecao, traceback) -> None:
        if self.__sessao is not None:
            self.__sessao.close()
            self.__sessao = None

        self.__mesa_service = None
        self.__produto_service = None
        self.__atendimento_service = None
        self.__pedido_service = None
        self.__pagamento_service = None

    @staticmethod
    def _exigir(valor):
        if valor is None:
            raise RuntimeError("A aplicação não foi inicializada.")
        return valor

    @property
    def sessao(self) -> Session:
        return self._exigir(self.__sessao)

    @property
    def mesa_service(self) -> MesaService:
        return self._exigir(self.__mesa_service)

    @property
    def produto_service(self) -> ProdutoService:
        return self._exigir(self.__produto_service)

    @property
    def atendimento_service(self) -> AtendimentoService:
        return self._exigir(self.__atendimento_service)

    @property
    def pedido_service(self) -> PedidoService:
        return self._exigir(self.__pedido_service)

    @property
    def pagamento_service(self) -> PagamentoService:
        return self._exigir(self.__pagamento_service)
