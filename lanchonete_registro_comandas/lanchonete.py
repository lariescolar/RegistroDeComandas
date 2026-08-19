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


class Lanchonete:
    """
    Representa a aplicação da Lanchonete.

    Responsável por manter mesas, produtos e atendimentos em memória
    e coordenar as operações do sistema.
    """

    def __init__(self) -> None:
        """Inicializa as coleções da aplicação."""
        self.__mesas: list[Mesa] = []
        self.__produtos: list[Produto] = []
        self.__atendimentos: list[Atendimento] = []

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
        """
        Cadastra uma mesa na lanchonete.

        Args:
            mesa: Mesa que será cadastrada.
        """
        self.__mesas.append(mesa)

    def cadastrar_produto(self, produto: Produto) -> None:
        """
        Cadastra um produto na lanchonete.

        Args:
            produto: Produto que será cadastrado.
        """
        self.__produtos.append(produto)

    def localizar_mesa(self, numero: int) -> Mesa | None:
        """
        Localiza uma mesa pelo número.

        Args:
            numero: Número da mesa.

        Returns:
            A mesa encontrada ou None caso não exista.
        """
        for mesa in self.__mesas:
            if mesa.numero == numero:
                return mesa

        return None

    def localizar_produto(self, codigo: int) -> Produto:
        """
        Localiza um produto pelo código.

        Args:
            codigo: Código do produto.

        Returns:
            O produto encontrado.

        Raises:
            ProdutoNaoEncontradoError: Caso o produto não exista.
        """
        for produto in self.__produtos:
            if produto.codigo == codigo:
                return produto

        raise ProdutoNaoEncontradoError("Produto não encontrado.")

    def abrir_atendimento(self, mesa: Mesa) -> Atendimento:
        """
        Abre um novo atendimento para uma mesa.

        Args:
            mesa: Mesa que receberá o atendimento.

        Returns:
            O atendimento criado.

        Raises:
            MesaOcupadaError: Caso a mesa já esteja ocupada.
        """
        if mesa.ocupada:
            raise MesaOcupadaError("A mesa já está ocupada.")

        atendimento = Atendimento(mesa)
        mesa.ocupar()
        self.__atendimentos.append(atendimento)
        return atendimento

    def localizar_atendimento(self, mesa: Mesa) -> Atendimento:
        """
        Localiza o atendimento aberto de uma mesa.

        Args:
            mesa: Mesa cujo atendimento será localizado.

        Returns:
            O atendimento aberto da mesa.

        Raises:
            AtendimentoNaoEncontradoError: Caso não exista atendimento aberto.
        """
        for atendimento in self.__atendimentos:
            if atendimento.mesa == mesa and not atendimento.encerrado:
                return atendimento

        raise AtendimentoNaoEncontradoError(
            "Não existe atendimento aberto para essa mesa."
        )

    def registrar_pedido(
        self,
        atendimento: Atendimento,
        pedido: Pedido
    ) -> None:
        """
        Registra um pedido em um atendimento.

        Args:
            atendimento: Atendimento que receberá o pedido.
            pedido: Pedido que será registrado.
        """
        atendimento.adicionar_pedido(pedido)

    def registrar_pagamento(
        self,
        atendimento: Atendimento,
        pagamento: Pagamento
    ) -> None:
        """
        Registra um pagamento em um atendimento.

        Args:
            atendimento: Atendimento que receberá o pagamento.
            pagamento: Pagamento que será registrado.
        """
        atendimento.registrar_pagamento(pagamento)

    def encerrar_atendimento(
        self,
        atendimento: Atendimento
    ) -> None:
        """
        Encerra um atendimento.

        Args:
            atendimento: Atendimento que será encerrado.
        """
        atendimento.encerrar()

    def consultar_atendimentos(self) -> list[Atendimento]:
        """
        Retorna os atendimentos registrados na lanchonete.

        Returns:
            Cópia da lista de atendimentos.
        """
        return self.__atendimentos.copy()
