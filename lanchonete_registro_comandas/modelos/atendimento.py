from modelos.mesa import Mesa
from modelos.pedido import Pedido
from modelos.pagamento import Pagamento

from excecoes.lanchonete_error import (
    AtendimentoEncerradoError,
    AtendimentoNaoQuitadoError,
    PagamentoInvalidoError,
)


class Atendimento:
    """Representa um atendimento de uma mesa,
    contendo pedidos e pagamentos."""

    def __init__(self, mesa: Mesa):
        self.__mesa: Mesa = mesa
        self.__pedidos: list[Pedido] = []
        self.__pagamentos: list[Pagamento] = []
        self.__encerrado: bool = False

    @property
    def mesa(self) -> Mesa:
        return self.__mesa

    @property
    def pedidos(self) -> list[Pedido]:
        return self.__pedidos.copy()

    @property
    def pagamentos(self) -> list[Pagamento]:
        return self.__pagamentos.copy()

    @property
    def encerrado(self) -> bool:
        return self.__encerrado

    @property
    def total(self) -> float:
        return sum(pedido.valor for pedido in self.__pedidos)

    @property
    def total_pago(self) -> float:
        return sum(pagamento.valor for pagamento in self.__pagamentos)

    @property
    def saldo(self) -> float:
        return self.total - self.total_pago

    def adicionar_pedido(self, pedido: Pedido) -> None:
        if self.__encerrado:
            raise AtendimentoEncerradoError(
                "Não é possível adicionar pedidos a um atendimento encerrado."
            )

        self.__pedidos.append(pedido)

    def registrar_pagamento(self, pagamento: Pagamento) -> None:
        if self.__encerrado:
            raise AtendimentoEncerradoError(
                "Não é possível registrar pagamentos em um atendimento encerrado."
            )

        if pagamento.valor <= 0:
            raise PagamentoInvalidoError(
                "O valor do pagamento deve ser maior que zero."
            )

        if pagamento.valor > self.saldo:
            raise PagamentoInvalidoError(
                "O pagamento não pode ser superior ao saldo da comanda."
            )

        self.__pagamentos.append(pagamento)

    def encerrar(self) -> None:
        if self.saldo > 0:
            raise AtendimentoNaoQuitadoError(
                "Não é possível encerrar um atendimento com saldo pendente."
            )

        self.__encerrado = True
        self.__mesa.liberar()

    def __str__(self) -> str:
        status = "Encerrado" if self.__encerrado else "Em aberto"
        return (
            f"Mesa {self.__mesa.numero} | {status} | "
            f"Total: R$ {self.total:.2f} | "
            f"Pago: R$ {self.total_pago:.2f} | "
            f"Saldo: R$ {self.saldo:.2f}"
        )
