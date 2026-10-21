from formatacao import formatar_moeda
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

    def __init__(self, mesa: Mesa, id_atendimento: int | None = None):
        self.__id: int | None = id_atendimento
        self.__mesa: Mesa = mesa
        self.__pedidos: list[Pedido] = []
        self.__pagamentos: list[Pagamento] = []
        self.__encerrado: bool = False

    @property
    def id(self) -> int | None:
        return self.__id

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
        """Soma dos valores dos pedidos, arredondada em centavos."""
        return round(sum(pedido.valor for pedido in self.__pedidos), 2)

    @property
    def total_pago(self) -> float:
        """Soma dos valores dos pagamentos, arredondada em centavos."""
        return round(sum(pagamento.valor for pagamento in self.__pagamentos), 2)

    @property
    def saldo(self) -> float:
        """Total menos o total pago, arredondado em centavos.

        O arredondamento evita que erros de ponto flutuante (ex.: 5.5e-17)
        sejam interpretados como saldo pendente.
        """
        return round(self.total - self.total_pago, 2)

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

    def to_dict(self) -> dict:
        return {
            "id": self.__id,
            "numero_mesa": self.__mesa.numero,
            "pedido_ids": [
                getattr(pedido, "id")
                for pedido in self.__pedidos
                if hasattr(pedido, "id")
            ],
            "pagamento_ids": [
                getattr(pagamento, "id")
                for pagamento in self.__pagamentos
                if hasattr(pagamento, "id")
            ],
            "encerrado": self.__encerrado,
        }

    @classmethod
    def from_dict(
        cls,
        dados: dict,
        mesa: Mesa,
        pedidos: list[Pedido] | None = None,
        pagamentos: list[Pagamento] | None = None,
    ) -> "Atendimento":
        atendimento = cls(mesa=mesa, id_atendimento=dados.get("id"))
        if pedidos:
            atendimento.__pedidos = pedidos
        if pagamentos:
            atendimento.__pagamentos = pagamentos
        atendimento.__encerrado = dados.get("encerrado", False)
        return atendimento

    def __str__(self) -> str:
        status = "Encerrado" if self.__encerrado else "Em aberto"
        situacao_mesa = "Bloqueada" if self.__mesa.bloqueada else "Desbloqueada"
        return (
            f"Mesa {self.__mesa.numero} ({situacao_mesa}) | {status} | "
            f"Total: {formatar_moeda(self.total)} | "
            f"Pago: {formatar_moeda(self.total_pago)} | "
            f"Saldo: {formatar_moeda(self.saldo)}"
        )
