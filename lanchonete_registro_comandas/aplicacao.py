"""Camada de aplicação da lanchonete.

Mantém os dados em memória e fornece acesso controlado às listas do sistema.
"""

from __future__ import annotations

from modelos.atendimento import Atendimento
from modelos.mesa import Mesa
from modelos.produto import Produto


class Lanchonete:
    """Representa a aplicação da lanchonete e suas coleções em memória."""

    def __init__(self) -> None:
        self.__mesas: list[Mesa] = []
        self.__produtos: list[Produto] = []
        self.__atendimentos: list[Atendimento] = []

    @property
    def mesas(self) -> list[Mesa]:
        """Retorna uma cópia das mesas cadastradas."""
        return self.__mesas.copy()

    @property
    def produtos(self) -> list[Produto]:
        """Retorna uma cópia dos produtos cadastrados."""
        return self.__produtos.copy()

    @property
    def atendimentos(self) -> list[Atendimento]:
        """Retorna uma cópia dos atendimentos registrados."""
        return self.__atendimentos.copy()

    def adicionar_mesa(self, mesa: Mesa) -> None:
        """Adiciona uma mesa à coleção interna."""
        self.__mesas.append(mesa)

    def adicionar_produto(self, produto: Produto) -> None:
        """Adiciona um produto à coleção interna."""
        self.__produtos.append(produto)

    def adicionar_atendimento(self, atendimento: Atendimento) -> None:
        """Adiciona um atendimento à coleção interna."""
        self.__atendimentos.append(atendimento)
