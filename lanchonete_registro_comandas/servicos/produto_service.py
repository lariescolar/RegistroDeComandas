"""Serviços relacionados aos produtos."""

from __future__ import annotations

from aplicacao import Lanchonete
from excecoes.lanchonete_error import ProdutoNaoEncontradoError
from modelos.produto import Produto


class ProdutoService:
    """Coordena as operações relacionadas aos produtos."""

    def __init__(self, aplicacao: Lanchonete) -> None:
        self.__aplicacao = aplicacao

    def cadastrar_produto(self, produto: Produto) -> None:
        """Cadastra um produto na aplicação."""
        self.__aplicacao.adicionar_produto(produto)

    def localizar_produto(self, codigo: int) -> Produto:
        """Localiza um produto pelo código."""
        for produto in self.__aplicacao.produtos:
            if produto.codigo == codigo:
                return produto
        raise ProdutoNaoEncontradoError("Produto não encontrado.")

    def listar_produtos(self) -> list[Produto]:
        """Retorna a lista de produtos cadastrados."""
        return self.__aplicacao.produtos
