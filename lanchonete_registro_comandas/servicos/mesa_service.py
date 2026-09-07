"""Serviços relacionados às mesas."""

from __future__ import annotations

from aplicacao import Lanchonete
from modelos.mesa import Mesa


class MesaService:
    """Coordena as operações relacionadas às mesas."""

    def __init__(self, aplicacao: Lanchonete) -> None:
        self.__aplicacao = aplicacao

    def cadastrar_mesa(self, mesa: Mesa) -> None:
        """Cadastra uma mesa na aplicação."""
        self.__aplicacao.adicionar_mesa(mesa)

    def localizar_mesa(self, numero: int) -> Mesa | None:
        """Localiza uma mesa pelo número."""
        for mesa in self.__aplicacao.mesas:
            if mesa.numero == numero:
                return mesa
        return None

    def listar_mesas(self) -> list[Mesa]:
        """Retorna a lista de mesas cadastradas."""
        return self.__aplicacao.mesas
