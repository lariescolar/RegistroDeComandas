"""Serviços relacionados aos produtos."""

import math

from sqlalchemy import select
from sqlalchemy.orm import Session

from excecoes.lanchonete_error import (
    DadoInvalidoError,
    ProdutoJaCadastradoError,
    ProdutoNaoEncontradoError,
)
from modelos.produto import Produto


class ProdutoService:
    """Coordena as operações relacionadas aos produtos."""

    def __init__(self, sessao: Session) -> None:
        self.__sessao = sessao

    def cadastrar_produto(
        self,
        classe: type[Produto],
        codigo: int,
        nome: str,
        preco: float,
        disponivel: bool = True,
    ) -> Produto:
        """Cadastra um produto do tipo informado (Suco, Sanduiche...)."""
        if classe is Produto or not issubclass(classe, Produto):
            raise DadoInvalidoError("Tipo de produto inválido.")

        nome = nome.strip()

        if not nome:
            raise DadoInvalidoError("O nome do produto não pode ser vazio.")

        if not math.isfinite(preco) or preco <= 0:
            raise DadoInvalidoError("O preço deve ser maior que zero.")

        if self.__sessao.get(Produto, codigo) is not None:
            raise ProdutoJaCadastradoError(
                "Já existe um produto com esse código."
            )

        produto = classe(
            codigo=codigo,
            nome=nome,
            preco=preco,
            disponivel=disponivel,
        )

        try:
            self.__sessao.add(produto)
            self.__sessao.commit()
        except Exception:
            self.__sessao.rollback()
            raise

        return produto

    def localizar_produto(self, codigo: int) -> Produto:
        """Localiza um produto pelo código (chave primária)."""
        produto = self.__sessao.get(Produto, codigo)

        if produto is None:
            raise ProdutoNaoEncontradoError("Produto não encontrado.")

        return produto

    def listar_produtos(self) -> list[Produto]:
        """Retorna os produtos cadastrados, ordenados pelo código."""
        comando = select(Produto).order_by(Produto.codigo)
        return list(self.__sessao.scalars(comando).all())
