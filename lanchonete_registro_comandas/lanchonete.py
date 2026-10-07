from modelos.mesa import Mesa
from modelos.produto import Produto
from modelos.atendimento import Atendimento
from modelos.pedido import Pedido
from modelos.pagamento import Pagamento

from excecoes.lanchonete_error import (
    AtendimentoNaoEncontradoError,
    MesaOcupadaError,
    ProdutoNaoEncontradoError,
)

from persistencia.produto_persistencia import ProdutoPersistencia
from persistencia.mesa_persistencia import MesaPersistencia
from persistencia.pedido_persistencia import PedidoPersistencia
from persistencia.pagamento_persistencia import PagamentoPersistencia
from persistencia.atendimento_persistencia import AtendimentoPersistencia


class Lanchonete:
    """
    Representa a aplicação da Lanchonete.
    Coordena as operações e a persistência em arquivos JSON.
    """

    def __init__(self) -> None:
        self.__mesas: list[Mesa] = []
        self.__produtos: list[Produto] = []
        self.__atendimentos: list[Atendimento] = []

        self.__produto_persistencia = ProdutoPersistencia()
        self.__mesa_persistencia = MesaPersistencia()
        self.__pedido_persistencia = PedidoPersistencia()
        self.__pagamento_persistencia = PagamentoPersistencia()
        self.__atendimento_persistencia = AtendimentoPersistencia()

        self.carregar_dados()

    def carregar_dados(self) -> None:
        """Carrega e reconstrói os objetos e seus relacionamentos a partir do JSON."""
        self.__produtos = self.__produto_persistencia.carregar_todos()
        self.__mesas = self.__mesa_persistencia.carregar_todas()

        pedidos = self.__pedido_persistencia.carregar_todos(self.__produtos)
        pagamentos = self.__pagamento_persistencia.carregar_todos()

        self.__atendimentos = self.__atendimento_persistencia.carregar_todos(
            mesas=self.__mesas,
            pedidos=pedidos,
            pagamentos=pagamentos,
        )

    def salvar_dados(self) -> None:
        """Garante a atribuição de IDs válidos e salva os dados nos ficheiros JSON."""
        self.__produto_persistencia.salvar_todos(self.__produtos)
        self.__mesa_persistencia.salvar_todas(self.__mesas)

        pedidos: list[Pedido] = []
        pagamentos: list[Pagamento] = []

        proximo_id_atendimento = 1
        proximo_id_pedido = 1
        proximo_id_pagamento = 1

        for atendimento in self.__atendimentos:
            if atendimento.id is None:
                atendimento._Atendimento__id = proximo_id_atendimento
            proximo_id_atendimento = max(proximo_id_atendimento, atendimento.id + 1)

            for pedido in atendimento.pedidos:
                if pedido.id is None:
                    pedido._Pedido__id = proximo_id_pedido
                proximo_id_pedido = max(proximo_id_pedido, pedido.id + 1)
                if pedido not in pedidos:
                    pedidos.append(pedido)

            for pagamento in atendimento.pagamentos:
                if pagamento.id is None:
                    pagamento._Pagamento__id = proximo_id_pagamento
                proximo_id_pagamento = max(proximo_id_pagamento, pagamento.id + 1)
                if pagamento not in pagamentos:
                    pagamentos.append(pagamento)

        self.__pedido_persistencia.salvar_todos(pedidos)
        self.__pagamento_persistencia.salvar_todos(pagamentos)
        self.__atendimento_persistencia.salvar_todos(self.__atendimentos)

    @property
    def mesas(self) -> list[Mesa]:
        return self.__mesas.copy()

    @property
    def produtos(self) -> list[Produto]:
        return self.__produtos.copy()

    @property
    def atendimentos(self) -> list[Atendimento]:
        return self.__atendimentos.copy()

    def cadastrar_mesa(self, mesa: Mesa) -> None:
        self.__mesas.append(mesa)
        self.salvar_dados()

    def cadastrar_produto(self, produto: Produto) -> None:
        self.__produtos.append(produto)
        self.salvar_dados()

    def localizar_mesa(self, numero: int) -> Mesa | None:
        for mesa in self.__mesas:
            if mesa.numero == numero:
                return mesa
        return None

    def localizar_produto(self, codigo: int) -> Produto:
        for produto in self.__produtos:
            if produto.codigo == codigo:
                return produto
        raise ProdutoNaoEncontradoError("Produto não encontrado.")

    def abrir_atendimento(self, mesa: Mesa) -> Atendimento:
        if mesa.ocupada:
            raise MesaOcupadaError("A mesa já está ocupada.")

        proximo_id = max([a.id for a in self.__atendimentos if a.id is not None], default=0) + 1
        atendimento = Atendimento(mesa, id_atendimento=proximo_id)
        mesa.ocupar()
        self.__atendimentos.append(atendimento)
        self.salvar_dados()
        return atendimento

    def localizar_atendimento(self, mesa: Mesa) -> Atendimento:
        for atendimento in self.__atendimentos:
            if atendimento.mesa == mesa and not atendimento.encerrado:
                return atendimento
        raise AtendimentoNaoEncontradoError("Não existe atendimento aberto para essa mesa.")

    def registrar_pedido(self, atendimento: Atendimento, pedido: Pedido) -> None:
        if pedido.id is None:
            todos_pedidos: list[Pedido] = []
            for a in self.__atendimentos:
                todos_pedidos.extend(a.pedidos)
            proximo_id = max([p.id for p in todos_pedidos if p.id is not None], default=0) + 1
            pedido._Pedido__id = proximo_id

        atendimento.adicionar_pedido(pedido)
        self.salvar_dados()

    def registrar_pagamento(self, atendimento: Atendimento, pagamento: Pagamento) -> None:
        if pagamento.id is None:
            todos_pagamentos: list[Pagamento] = []
            for a in self.__atendimentos:
                todos_pagamentos.extend(a.pagamentos)
            proximo_id = max([pg.id for pg in todos_pagamentos if pg.id is not None], default=0) + 1
            pagamento._Pagamento__id = proximo_id

        atendimento.registrar_pagamento(pagamento)
        self.salvar_dados()

    def encerrar_atendimento(self, atendimento: Atendimento) -> None:
        atendimento.encerrar()
        self.salvar_dados()

    def consultar_atendimentos(self) -> list[Atendimento]:
        return self.__atendimentos.copy()
