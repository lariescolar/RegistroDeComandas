"""Serviços relacionados aos atendimentos."""

from __future__ import annotations

from aplicacao import Lanchonete
from excecoes.lanchonete_error import (
    AtendimentoEncerradoError,
    AtendimentoNaoEncontradoError,
    AtendimentoNaoQuitadoError,
    MesaOcupadaError,
    PagamentoInvalidoError,
)
from modelos.atendimento import Atendimento
from modelos.mesa import Mesa


class AtendimentoService:
    """Coordena as operações relacionadas aos atendimentos."""

    def __init__(self, aplicacao: Lanchonete) -> None:
        self.__aplicacao = aplicacao

    def abrir_atendimento(self, mesa: Mesa) -> Atendimento:
        """Abre um novo atendimento para a mesa informada."""
        if mesa.ocupada:
            raise MesaOcupadaError("A mesa já possui um atendimento em andamento.")

        atendimento = Atendimento(mesa)
        mesa.ocupar()
        self.__aplicacao.adicionar_atendimento(atendimento)
        return atendimento

    def localizar_atendimento(self, mesa: Mesa) -> Atendimento:
        """Localiza o atendimento em aberto da mesa informada."""
        for atendimento in self.__aplicacao.atendimentos:
            if atendimento.mesa == mesa and not atendimento.encerrado:
                return atendimento

        raise AtendimentoNaoEncontradoError(
            "Não existe atendimento aberto para essa mesa."
        )

    def encerrar_atendimento(self, atendimento: Atendimento) -> None:
        """Encerra um atendimento, se ele estiver quitado."""
        atendimento.encerrar()

    def consultar_historico(self) -> list[Atendimento]:
        """Retorna todos os atendimentos registrados."""
        return self.__aplicacao.atendimentos
